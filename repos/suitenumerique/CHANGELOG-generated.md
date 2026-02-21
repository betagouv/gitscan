# Synthèse d'activité : suitenumerique (derniers 7 jours)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité soutenue, avec des améliorations significatives apportées à plusieurs de ses applications. Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités comme l'importation de calendriers ([calendars](/repos/suitenumerique/calendars)), le mode sombre persistant ([conversations](/repos/suitenumerique/conversations)), et l'importation de fichiers PST ([messages](/repos/suitenumerique/messages)). Des améliorations de sécurité ont également été apportées, notamment la correction de vulnérabilités XSS dans [projects](/repos/suitenumerique/projects) et [meet](/repos/suitenumerique/meet), ainsi que des mises à jour de dépendances pour corriger des failles de sécurité. L'accent a été mis sur la stabilisation des fonctionnalités (sortie de la version 1 de la visioconférence dans [integration](/repos/suitenumerique/integration)) et l'amélioration de la performance, en particulier dans [conversations](/repos/suitenumerique/conversations).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction d'une vulnérabilité XSS dans [projects](/repos/suitenumerique/projects).
- Correction d'une vulnérabilité XSS dans [meet](/repos/suitenumerique/meet).
- Mises à jour de dépendances pour corriger des failles de sécurité dans [people](/repos/suitenumerique/people) et [st-deploycenter](/repos/suitenumerique/st-deploycenter).
- Mise à jour de Django et d'OpenSSL dans [meet](/repos/suitenumerique/meet) pour corriger des vulnérabilités critiques.

## Autres changements notables
- Refonte de l'interface utilisateur de [calendars](/repos/suitenumerique/calendars) et ajout de nombreuses nouvelles fonctionnalités.
- Migration vers `uv` pour améliorer les performances du backend de [conversations](/repos/suitenumerique/conversations).
- Ajout de la variable `st_keycloak_start_command` dans [st-ansible](/repos/suitenumerique/st-ansible) pour une configuration plus flexible de Keycloak.
- Refactorisation des résolveurs de droits dans [st-deploycenter](/repos/suitenumerique/st-deploycenter) pour une meilleure gestion des autorisations.
- Configuration de Nginx en front-end de Next.js dans [st-home](/repos/suitenumerique/st-home) pour une meilleure performance et sécurité.

## Dépôts les plus actifs
- [calendars](/repos/suitenumerique/calendars) : Refonte majeure de l'interface utilisateur et ajout de nombreuses nouvelles fonctionnalités pour la gestion des calendriers et des événements.
- [conversations](/repos/suitenumerique/conversations) : Amélioration de l'expérience utilisateur avec le mode sombre persistant, une meilleure gestion des fichiers et des optimisations de performance.
- [messages](/repos/suitenumerique/messages) : Ajout de l'importation de fichiers PST et de l'exportation de boîtes aux lettres au format MBOX.
- [projects](/repos/suitenumerique/projects) : Ajout d'indicateurs de nombre d'éléments dans les listes et amélioration de l'assignation automatique de membres et de labels.
- [meet](/repos/suitenumerique/meet) : Amélioration de l'accessibilité et correction de vulnérabilités de sécurité.
- [ui-kit](/repos/suitenumerique/ui-kit) : Ajout de nouveaux composants (menu contextuel, modal d'onboarding) et améliorations des composants existants.
