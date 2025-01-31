import json
import time
import random
import typer
from googlesearch import search
from rich.console import Console
from rich.progress import Progress

console = Console()
app = typer.Typer(add_completion=False)

def search_and_save(
    dorks_file: str,
    domain: str,
    output_file: str,
    num_results: int = 10,
    delay_range: tuple = (2, 5),
):
    try:
        with open(dorks_file, "r") as file:
            dorks = file.readlines()
    except FileNotFoundError:
        console.print(
            f"[bold red]Error:[/bold red] The file '{dorks_file}' was not found."
        )
        return

    results = []

    with Progress() as progress:
        task = progress.add_task("[cyan]Searching...", total=len(dorks))

        for dork in dorks:
            dork = dork.strip()
            query = f"{dork} site:{domain}"

            console.print(f"[bold green]Searching for:[/bold green] {query}")

            try:

                search_results = search(query, num_results=num_results)

                if search_results:
                    for result in search_results:
                        results.append({"dork": dork, "result": result})

                delay = random.uniform(*delay_range)
                console.print(
                    f"[yellow]Waiting for {delay:.2f} seconds before the next search...[/yellow]"
                )
                time.sleep(delay)

            except Exception as e:
                console.print(
                    f"[bold red]An error occurred while searching for '{query}':[/bold red] {e}"
                )

            progress.update(task, advance=1)

    try:
        with open(output_file, "w") as json_file:
            json.dump(results, json_file, indent=4)
        console.print(f"[bold green]Results saved to[/bold green] {output_file}")
    except Exception as e:
        console.print(
            f"[bold red]An error occurred while saving the results:[/bold red] {e}"
        )


@app.command()
def main(
    dorks_file: str = typer.Option(..., help="File containing dorks to search."),
    domain: str = typer.Option(..., help="The target domain to search within."),
    output_file: str = typer.Option(
        ..., help="Output file to save the search results."
    ),
    num_results: int = typer.Option(
        10, help="Number of results to retrieve per search."
    ),
    delay_range: str = typer.Option(
        "2,5", help="Delay range (min,max) in seconds between requests."
    ),
):
    delay_range_tuple = tuple(map(int, delay_range.split(",")))
    search_and_save(dorks_file, domain, output_file, num_results, delay_range_tuple)


app()
