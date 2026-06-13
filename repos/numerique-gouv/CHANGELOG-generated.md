# Synthèse d'activité : numerique-gouv (du 29 avril au 12 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation numerique-gouv s'est concentrée sur l'amélioration de la robustesse et de l'expérience utilisateur de ses différentes plateformes. Plusieurs dépôts ont bénéficié d'améliorations d'internationalisation, notamment [sites-faciles](/repos/numerique-gouv/sites-faciles) et [sites-faciles-fork-1](/repos/numerique-gouv/sites-faciles-fork-1), avec l'ajout de la gestion de plusieurs langues et de sélecteurs de langue. Des efforts importants ont également été déployés pour renforcer la sécurité avec l'intégration de Sentry dans [sites-conformes](/repos/numerique-gouv/sites-conformes) et la mise à jour de dépendances critiques dans [django-dsfr](/repos/numerique-gouv/django-dsfr) et [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage). Enfin, des améliorations significatives ont été apportées à [b3desk](/repos/numerique-gouv/b3desk) pour la gestion des réunions et des utilisateurs.

## Sécurité
- Mise à jour de Next.js et PostCSS dans [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) pour corriger des failles de sécurité.
- Mise à jour des dépendances dans [django-dsfr](/repos/numerique-gouv/django-dsfr) pour améliorer la sécurité.

## Autres changements notables
- Intégration de Sentry pour la surveillance des erreurs dans [sites-conformes](/repos/numerique-gouv/sites-conformes).
- Mise en place d'un déploiement en un clic sur Scalingo pour [sites-faciles](/repos/numerique-gouv/sites-faciles).
- Refonte de l'architecture de l'administration dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Mise en place d'une réplication de la base de données vers un datawarehouse dans [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api).
- Adoption de la couleur d'accent par défaut du DSFR pour SwiftUI et UIKit dans [ami-design-system-ios](/repos/numerique-gouv/ami-design-system-ios).

## Dépôts les plus actifs
- [sites-faciles](/repos/numerique-gouv/sites-faciles) : Ajout de la gestion de plusieurs langues et simplification du déploiement.
- [sites-conformes](/repos/numerique-gouv/sites-conformes) : Amélioration de la robustesse avec l'intégration de Sentry et la possibilité de stocker les médias en PostgreSQL.
- [b3desk](/repos/numerique-gouv/b3desk) : Amélioration de la gestion des réunions et des utilisateurs, avec automatisation de la publication des releases.
- [ami-notifications-api](/repos/numerique-gouv/ami-notifications-api) : Amélioration de l'expérience utilisateur mobile et refonte de l'administration.
- [lasuite-landingpage](/repos/numerique-gouv/lasuite-landingpage) : Ajout d'informations sur Resana 2027 et ajout des pages légales.
