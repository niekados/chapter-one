# Chapter One

<img src="" alt="Am I Responsive" style="width:90%;">

"Chapter One" is an online bookstore designed to support emerging authors by providing them with a platform to share their work. Focused on selling affordable, digital PDF books, Chapter One aims to connect readers with fresh voices in literature, offering them a unique way to support new authors at the start of their writing journey. With a minimalist design, integrated Stripe payments, and Mailchimp newsletters, Chapter One fosters an accessible environment for both authors and readers passionate about discovering new stories.

**[Link to the deployed application]()**

## Index

- [Project Inception](#project-inception)
- [Customer Goals](#customer-goals)
- [Business Goals](#business-goals)
- [User Stories](#user-stories)
- [Strategy](#strategy)
- [Scope](#scope)
- [Structure](#structure)
- [Skeleton](#skeleton)
  - [Wireframes](#wireframes)
- [Surface](#surface)
    - [Fonts](#fonts)
    - [Colours](#colours)
- [Security](#security)
- [Features](#features)
- [Future Features](#future-features)
- [Database Schema](#database-schema)
  -[Entity Relationship Diagram](#entity-relationship-diagram)
- [Agile](#agile)
  - [MoSCoW Prioritization](#moscow-prioritization)
  - [Sprints](#sprints)
- [Marketing](#marketing)
- [Deploying Project to Heroku](#deploying-project-to-heroku)


  - [Google Mail Setup](#google-mail-setup)
  - [AWS Config](#aws-config)
    - [Media Folder Setup](#media-folder-setup)
    - [Django AWS Connect](#django-aws-connect)
  - [Stripe Config](#stripe-config)

  
- [Technologies Used](#technologies-used)
- [Credits](#credits)
- [Testing](#testing)

## Project Inception

Chapter One was created with a vision to support and uplift undiscovered writers. The traditional publishing world often presents barriers for new authors, making it difficult to reach an audience or gain financial backing. Chapter One is here to change that, offering a minimalist digital platform where emerging writers can share their works, and readers can support them directly by purchasing their books.

The platform is simple yet impactful, designed to encourage new talent and foster a community of readers who value fresh perspectives. Readers can explore short stories and digital books in various genres, knowing that each purchase directly supports a writer at the beginning of their creative journey.

## Customer Goals

**Chapter One** is designed with two primary customers in mind: new authors and readers who are eager to discover unique literary voices. The platform’s goal is to serve both groups by creating an accessible, encouraging environment that benefits everyone involved.

### For Authors
- **Visibility**: Provide a space for emerging authors to showcase their work to a wider audience.
- **Financial Support**: Enable authors to earn revenue through direct sales of their digital books.
- **Encouragement**: Offer a platform where writers can feel valued and build confidence in their craft.

### For Readers
- **Discovery**: Give readers a curated space to find fresh stories from new voices in literature.
- **Support for New Authors**: Allow readers to support emerging talent directly, contributing to the growth of a writer’s career.
- **Convenience**: Provide a simple, enjoyable experience for browsing, purchasing, and accessing digital books in one place.

## Business Goals

The mission of **Chapter One** is to bridge the gap between emerging authors and readers, providing a mutually beneficial platform that supports creative growth and discovery. The business goals are designed to ensure a sustainable and engaging marketplace for both authors and readers, fostering a community that values fresh literary voices.

### Key Business Goals

- **Support New Authors**: Offer a low-cost platform where new authors can publish and monetize their work without the need for traditional publishing contracts.
  
- **Revenue Generation**: Establish a streamlined revenue model through direct book sales, with **Chapter One** taking a small commission to sustain platform operations while ensuring authors receive a fair share.

- **Encourage Reader Engagement**: Create an enjoyable, simple shopping experience that attracts readers interested in unique stories, fostering loyalty and frequent returns to the platform.

- **Build Brand Recognition**: Grow **Chapter One**'s reputation as the go-to place for discovering undiscovered writers, leveraging social media, Mailchimp newsletters, and community outreach to attract both authors and readers.

## Strategy

The strategy for **Chapter One** focuses on creating a welcoming platform where emerging authors can reach readers who are interested in discovering fresh literary talents. Key strategic points are centered on platform simplicity, user engagement, and long-term growth.

### Strategic Objectives

- **Simplicity and Accessibility**: Offer a minimalist design and easy navigation, making it intuitive for readers and authors to use. This includes straightforward features, a clear purchase flow, and minimal clicks to buy and access books.

- **Support New Authors**: Keep publishing costs low to attract new writers who may not have access to traditional publishing channels, fostering a community of emerging talent. 

- **Engage and Retain Readers**: Encourage user retention through a library feature for purchased books and regular updates about new releases through a Mailchimp-powered newsletter.

- **Revenue Growth with Digital-Only Sales**: Utilize Stripe integration to facilitate quick, secure purchases of digital content, keeping costs low while focusing on selling PDF books only.

- **Community Building and Marketing**: Use social media platforms, particularly Facebook, to connect with a broader audience, share author stories, and increase awareness of the platform as a place for discovering unique stories.

## Scope

The scope of **Chapter One** is to deliver a simple, functional platform for both readers and emerging authors. It focuses on core features to provide a positive user experience while staying aligned with the platform's mission.

- **Home Page**: Welcoming layout with a famous author quote used in place of a hero image, adding a literary atmosphere. Brief project description and a contact form for authors interested in publishing.
- **Books Page**: Catalog of available books with CSS-styled covers, searchable by title or genre.
- **Shopping Bag**: Feature allowing readers to add books to their cart and proceed to checkout.
- **My Library**: Personalized page where users can access and download previously purchased books.
- **Profile Page**: User account area with personal details and billing information.
- **Admin Page**: Access for site owners to add and manage book listings.
- **Secure Payments**: Integrated with Stripe for secure digital purchases.
- **Newsletter Subscription**: Mailchimp integration to keep readers updated on new books and authors.
- **Social Media Integration**: Facebook page and other social links to advertise new releases and engage readers.

