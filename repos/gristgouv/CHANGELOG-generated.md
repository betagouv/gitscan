# Synthèse d'activité : gristgouv (derniers 7 jours)

## Résumé de l'activité
L'activité de l'organisation gristgouv au cours des derniers jours s'est concentrée sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités à Grist. L'importation depuis Airtable a été significativement améliorée dans [grist-core](/repos/gristgouv/grist-core), et une nouvelle interface pour les déclencheurs d'automatisation a été introduite.  L'ajout d'un éditeur de texte enrichi et d'un widget "Formulaire Intra" ([grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) et [widgets-config](/repos/gristgouv/widgets-config)) renforce la capacité de Grist à gérer des données complexes et à s'intégrer à des workflows administratifs.  Des mises à jour de l'image Docker ([grist-docker-image](/repos/gristgouv/grist-docker-image)) et du contenu de formation ([grist-mooc](/repos/gristgouv/grist-mooc)) complètent cette période d'activité.

## Sécurité
Le dépôt [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) a bénéficié d'un renforcement de la sécurité avec l'implémentation de DOMPurify pour la sanitisation du contenu HTML et la prévention des attaques XSS.

## Autres changements notables
- Une migration complète de l'interface de développement vers Vue.js a été réalisée dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).
- Des corrections de tests aléatoires ont été implémentées dans [grist-core](/repos/gristgouv/grist-core) pour améliorer la fiabilité de la suite de tests.
- La recherche d'utilisateurs via le protocole SCIM a été accélérée dans [grist-core](/repos/gristgouv/grist-core).

## Dépôts les plus actifs
- [grist-core](/repos/gristgouv/grist-core) : Améliorations significatives de l'importation Airtable, nouvelle interface pour les déclencheurs d'automatisation et corrections de tests.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Ajout d'un éditeur de texte enrichi, amélioration de la validation des formulaires et migration vers Vue.js.
- [gristlabs-widgets](/repos/gristlabs/gristlabs-widgets) : Amélioration du widget calendrier et ajout d'un jeu expérimental "Whack-a-cell".
