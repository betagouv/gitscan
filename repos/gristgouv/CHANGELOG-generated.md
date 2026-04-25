# Synthèse d'activité : gristgouv (derniers 7 jours)

## Résumé de l'activité
La semaine écoulée a été marquée par des améliorations continues sur la plateforme Grist, avec un accent sur l'importation de données depuis Airtable, l'accessibilité des formulaires et la stabilité générale. L'ajout de nouveaux widgets et la mise à jour des contenus de formation renforcent l'offre pour les utilisateurs et les développeurs. L'équipe a également travaillé sur l'amélioration de l'expérience utilisateur pour les abonnements SaaS et l'intégration de formulaires internes.

## Sécurité
- Renforcement de la sécurité avec l'implémentation de DOMPurify pour la sanitisation du contenu HTML et la prévention des attaques XSS dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).

## Autres changements notables
- Refactorisation du code dans [grist-core](/repos/gristgouv/grist-core) pour séparer les tests spécifiques à l'édition Enterprise du cœur du projet.
- Migration de l'interface de développement vers Vue.js dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).
- Mise à jour de l'image Docker vers la version 1.7.12 dans [grist-docker-image](/repos/gristgouv/grist-docker-image).

## Dépôts les plus actifs
- [grist-core](/repos/gristgouv/grist-core) : Amélioration de la stabilité, correction de tests, et ajout de fonctionnalités d'importation Airtable et d'automatisation.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Ajout d'un éditeur de texte enrichi, amélioration de la validation des formulaires et renforcement de la sécurité.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour des contenus de formation avec de nouveaux exercices et instructions.
- [gristlabs-widgets](/repos/gristlabs/gristlabs-widgets) : Amélioration du widget calendrier et ajout d'un jeu expérimental "Whack-a-cell".
