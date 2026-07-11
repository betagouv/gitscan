# Synthèse d'activité : betagouv (du 24 mai au 24 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation betagouv a été marquée par une forte concentration sur l'amélioration de l'expérience utilisateur et la correction de bugs dans de nombreux projets. Plusieurs projets ont bénéficié de mises à jour significatives, notamment *mon-profil-anssi* avec une amélioration de la recherche, *jeveuxaider-front* avec une refonte des formulaires d'inscription, et *infomedicament* avec une recherche sémantique améliorée.  De nombreux efforts ont également été consacrés à la maintenance technique, à la sécurité et à l'optimisation des performances, notamment dans les projets *nitrates*, *mes-aides-analytics* et *grist-utils*. L'intégration de nouvelles sources de données et l'amélioration de la synchronisation entre différents systèmes ont également été des thèmes récurrents.

## Sécurité
Plusieurs projets ont bénéficié d'améliorations de sécurité :
- Correction d'une vulnérabilité critique dans [mon-suivi-justice](/repos/betagouv/mon-suivi-justice) avec une mise à jour de la gem `rack-session`.
- Renforcement de la sécurité dans [maestro](/repos/betagouv/maestro) avec la correction de failles XSS et la protection contre le détournement de compte.
- Amélioration de la sécurité du parseur [infomedicament-html-parser](/repos/betagouv/infomedicament-html-parser) avec des mises à jour de dépendances.

## Autres changements notables
- Migration vers React 19 et Turbopack dans [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) pour améliorer les performances.
- Refactorisation de l'infrastructure de [infomedicament-dataeng](/repos/betagouv/infomedicament-dataeng) avec le remplacement des bibliothèques de base de données par SQLAlchemy.
- Passage à Poetry pour la gestion des dépendances dans [infomedicament-dataeng](/repos/betagouv/infomedicament-dataeng) et [grist-utils](/repos/betagouv/grist-utils).
- Intégration de Matomo pour le suivi des événements dans [odice](/repos/betagouv/odice) et [infomedicament](/repos/betagouv/infomedicament).
- Mise en place d'un système de publication "trusted" pour [lab-anssi-lib](/repos/betagouv/lab-anssi-lib).

## Dépôts les plus actifs
- [maestro](/repos/betagouv/maestro) : Amélioration significative de l'interface utilisateur et de la gestion des données.
- [infomedicament](/repos/betagouv/infomedicament) : Amélioration de la recherche sémantique et de l'affichage des informations.
- [jeveuxaider-front](/repos/betagouv/jeveuxaider-front) : Refonte des formulaires d'inscription et amélioration de l'expérience utilisateur.
- [mon-profil-anssi](/repos/betagouv/mon-profil-anssi) : Amélioration de la recherche de profils et correction de vulnérabilités.
- [infomedicament-dataeng](/repos/betagouv/infomedicament-dataeng) : Amélioration de la gestion des données et de la recherche sémantique.
- [grist-custom-widgets-fr-admin](/repos/betagouv/grist-custom-widgets-fr-admin) : Préparation de la publication du widget "Tableau de bord cartographique".
