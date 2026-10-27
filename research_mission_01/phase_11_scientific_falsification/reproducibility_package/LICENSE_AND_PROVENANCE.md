# License & Task Provenance Disclosure

## License
The code and analysis scripts in this package are released under the MIT License.
The dataset and metadata are released under the Creative Commons Attribution 4.0 International (CC BY 4.0) License.

## Task Provenance Disclosure
The 20 evaluation problems in this package are **not** official GSM8K benchmark problems. They are synthetic arithmetic word problems inspired by GSM8K-style multi-step reasoning, constructed using a controlled parametric template:
`"A commercial store sells X notebooks per hour. If they operate for Y hours and sell each notebook for $4, what is the total revenue in dollars?"`

This design eliminates pretraining web scrape contamination and guarantees exact prospective matching between control and recovery prefixes.
