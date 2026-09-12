# Synthèse d'activité : gristgouv (du 10/07 au 17/07)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur l'enrichissement des capacités de visualisation et l'amélioration de l'expérience utilisateur. L'introduction de nouveaux widgets basés sur la librairie D3.js via [widgets-config](/repos/gristgouv/widgets-config) et la refonte majeure de l'ergonomie de [grist-widget-grouped-view](/repos/gristgouv/grist-widget-grouped-view) offrent des possibilités de présentation de données plus riches, personnalisables et accessibles.

Parallèlement, l'expérience de travail est optimisée par des ajustements de l'interface dans [grist-core](/repos/gristgouv/grist-core) et une mise à jour des ressources pédagogiques dans [grist-mooc](/repos/gristgouv/grist-mooc) pour faciliter l'auto-formation des utilisateurs.

## Sécurité
- Amélioration de la robustesse de l'affichage via la sanitisation des titres et le rendu en texte brut des données pour éviter les erreurs d'interprétation HTML ([gristlabs-widgets](/repos/gristgouv/gristlabs-widgets)).

## Autres changements notables
- Mise en conformité avec les standards d'accessibilité WCAG 2.1 AA ([grist-widget-grouped-view](/repos/gristgouv/grist-widget-grouped-view)).
- Optimisation de la gestion du trafic via l'introduction du proxying Grist Fleet ([grist-core](/repos/gristgouv/grist-core)).
- Mise en place de tests automatisés (smoke tests) pour assurer la stabilité du code ([grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form)).
- Mise à jour des images Docker vers les dernières versions stables de l'application ([grist-docker-image](/repos/gristgouv/grist-docker-image)).

## Dépôts les plus actifs
- [grist-widget-grouped-view](/repos/gristgouv/grist-widget-grouped-view) : Refonte majeure incluant l'internationalisation, l'accessibilité et de nouvelles options de personnalisation.
- [grist-core](/repos/gristgouv/grist-core) : Évolutions de l'interface utilisateur, de la gestion du trafic et de la documentation.
- [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) : Amélioration de la robustesse de l'affichage et de la gestion des erreurs.
