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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
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

<!-- USAGE EXAMPLES -->
## Usage
Open your browser and type in search bar `localhost:5000` or in command line `curl localhost:5000`

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

* `flake8-markdown` for `md` files
* `pylama` for `py` files

<!-- CONTACT -->
## Contact

Your Name - [@validolchik](https://t.me/validolchik) - r.valeev@innopolis.university

Project Link: [https://github.com/validolchik/devops](https://github.com/validolchik/devops)



[comment]: <> (<!-- ACKNOWLEDGEMENTS -->)

[comment]: <> (## Acknowledgements)

[comment]: <> (* [GitHub Emoji Cheat Sheet]&#40;https://www.webpagefx.com/tools/emoji-cheat-sheet&#41;)

[comment]: <> (* [Img Shields]&#40;https://shields.io&#41;)

[comment]: <> (* [Choose an Open Source License]&#40;https://choosealicense.com&#41;)

[comment]: <> (* [GitHub Pages]&#40;https://pages.github.com&#41;)

[comment]: <> (* [Animate.css]&#40;https://daneden.github.io/animate.css&#41;)

[comment]: <> (* [Loaders.css]&#40;https://connoratherton.com/loaders&#41;)

[comment]: <> (* [Slick Carousel]&#40;https://kenwheeler.github.io/slick&#41;)

[comment]: <> (* [Smooth Scroll]&#40;https://github.com/cferdinandi/smooth-scroll&#41;)

[comment]: <> (* [Sticky Kit]&#40;http://leafo.net/sticky-kit&#41;)

[comment]: <> (* [JVectorMap]&#40;http://jvectormap.com&#41;)

[comment]: <> (* [Font Awesome]&#40;https://fontawesome.com&#41;)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png