![Test build push](https://github.com/validolchik/devops/actions/workflows/work.yml/badge.svg)
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
        <ul>
          <li><a href="#Github">Github</a></li>
          <li><a href="#Docker">Docker</a></li>
        </ul>
      </ul>
    </li>
    <li>
      <a href="#unit-tests">Unit tests</a>
      <ul>
        <li><a href="#tests">Tests</a></li>
        <li><a href="#best-practices">Best practices</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#linters">Linters</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With


* Python 3.8.5
* Flask 1.1.2


<!-- GETTING STARTED -->

## Prerequisites
* Python 3.5+
* pip 21.2.4
* Flask
  ```sh
  pip install flask
  ```
  or
* ```sh
  pip3 install -r requirements.txt
  ```
## Installation

### GitHub
```sh
git clone https://github.com/validolchik/devops
cd app_python
python -m flask run
```

### Docker
```sh
docker pull validolchik/devops
docker run validolchik/devops -p 5000:5000
```

<!-- HOW TO TEST APPLICATION -->
## Unit tests
`pytest` was used to unit test the application
Run `python -m pytest` inside `app_python`
### Tests
1. `test_connection` checks whether app is alive and responding successfully to requests
2. `test_date_correctness` checks that app return correct time for Moscow
3. `test_factory` checks, whether app factory correctly parses the config file and creates test app when config is given
### Best practices
* Each test in separate file
* Tests are in separate folder
* Using `pytest` fixtures
* Each test tests separate thing
* Did not modify fixture inside another fixture
* Setup using `setup.py`, which allows installing packages in 'editable' mode


<!-- USAGE EXAMPLES -->
## Usage
Open your browser and type in search bar `localhost:5000` or in command line `curl localhost:5000`

To get main page visit timestamps, enter `localhost:5000/visits` 

Using this app you can know current time in Moscow, Russia

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LINTERS -->
## Linters

* `flake8-markdown` for python code inside the `md` files
  ```sh
  flake8-markdown *name of md file*.md
  ```
* `pylama` for `py` files
  ```sh
  pylama *.py
  ```
* `hadolint`
  ```sh
  docker pull hadolint/hadolint
  docker run --rm -i hadolint/hadolint < app_python/Dockerfile
  ```

<!-- CONTACT -->
## Contact

Renat Valeev - [@validolchik](https://t.me/validolchik) - r.valeev@innopolis.university

Project Link: [https://github.com/validolchik/devops](https://github.com/validolchik/devops)
