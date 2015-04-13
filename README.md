# Add a License Please

A bot that crawls Github for projects without any license, and asks the owner to add a license.

![](https://raw.githubusercontent.com/karan/add-a-license-please/master/logo.jpg)

Github is full of "open source" project that carry no explicit license. This bot will create an issue in repositories that are missing a license.

### Why include a license?

> Generally speaking, the absence of a license means that the default copyright laws apply. This means that you retain all rights to your source code and that nobody else may reproduce, distribute, or create derivative works from your work. This might not be what you intend.

Source: https://help.github.com/articles/open-source-licensing/

### How does it work?

The bot searches Github for repositories that have some stars (although the star restriction is a bit wonky). For the returned repos, it will check to see existence of any license information. If it's missing, it will create an issue in the repo. Simple!

### Where is this bot running?

Currently I'm running this bot on a 1GB [DigitalOcean](https://www.digitalocean.com/?refcode=422889a8186d) instance (yes, that's an affiliate link. Use that to get free VPS for 2 months). The bot is low of resources and uses a couple MB of RAM.
