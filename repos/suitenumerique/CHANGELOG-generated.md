# Synthèse d'activité : suitenumerique (du 22 mai au 11 juin 2026)

## Résumé de l'activité
L'organisation suitenumerique a connu une période d'activité soutenue, marquée par des améliorations significatives de ses produits phares. Les efforts se sont concentrés sur l'amélioration de la sécurité, notamment avec des mises à jour de dépendances et la correction de vulnérabilités. Plusieurs applications ont bénéficié de refontes techniques majeures, comme le passage de Next.js à Vite pour *calendars* et *conversations*, visant à optimiser les performances et l'expérience de développement. Des fonctionnalités importantes ont été ajoutées, comme la génération de liens de téléchargement uniques pour *st-transfers*, la suppression de dossiers dans *projects*, et l'amélioration de la gestion des RSVP dans *calendars*. L'accent a également été mis sur l'amélioration de l'expérience utilisateur, avec des corrections de bugs et des améliorations de l'interface dans de nombreux dépôts, notamment *hub*, *docs*, et *drive*.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :

- Correction de vulnérabilités dans les dépendances de *people* (urllib3, next, django, dimail).
- Renforcement de la sécurité du traitement des données ICS dans *calendars*.
- Correction d'une vulnérabilité potentielle dans *conversations* concernant l'exposition du port interne lors de la redirection OIDC.
- Amélioration de la sécurité avec `secrets.compare_digest` dans *dictaphone*.

## Autres changements notables
Plusieurs refactorings et migrations importantes ont eu lieu :

- Migration du frontend de *calendars* et *conversations* vers Vite pour une meilleure performance.
- Refonte de la gestion des RSVP dans *calendars*.
- Refonte du frontend de *hub* avec Next.js et TypeScript.
- Remplacement de Next.js par Vite et TanStack Router dans *messages* pour une meilleure performance et maintenabilité.
- Suppression de la recherche par embedding dans *find* pour se concentrer sur BM25.
- Amélioration de l'infrastructure de surveillance de la santé des modèles d'IA dans *conversations*.

## Dépôts les plus actifs
- [ui-kit](/repos/suitenumerique/ui-kit) : Amélioration de l'accessibilité et mise à jour de la bibliothèque d'icônes.
- [st-home](/repos/suitenumerique/st-home) : Corrections et améliorations de l'affichage des données et de la recherche de collectivités.
- [messages](/repos/suitenumerique/messages) : Refonte technique majeure avec migration vers Vite et TanStack Router, et ajout de nombreuses améliorations fonctionnelles.
- [calendars](/repos/suitenumerique/calendars) : Refonte de la gestion des RSVP et migration vers Vite.
- [conversations](/repos/suitenumerique/conversations) : Améliorations de la stabilité, de la sécurité et de l'expérience utilisateur, ainsi que migration vers Vite.
- [drive](/repos/suitenumerique/drive) : Ajout de l'export de dossiers et amélioration de la gestion des comptes.
- [docs](/repos/suitenumerique/docs) : Amélioration de la recherche et ajout d'un mode présentateur.
