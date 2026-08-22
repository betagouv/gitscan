# Synthèse d'activité : gristgouv (du 13/03 au 06/08)

## Résumé de l'activité
L'activité récente est marquée par un enrichissement des capacités de visualisation et une amélioration de la robustesse de l'interface. L'intégration de nouveaux widgets basés sur D3.js dans [widgets-config](/repos/gristgouv/widgets-config) et la refonte ergonomique du widget de vue groupée dans [grist-widget-grouped-view](/repos/gristgouv/grist-widget-grouped-view) offrent des possibilités de présentation de données plus riches et plus personnalisables pour les utilisateurs.

Parallèlement, la fiabilité de l'affichage est renforcée dans [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) et l'expérience utilisateur est améliorée dans [grist-core](/repos/gristgouv/grist-core) via de nouvelles options de personnalisation de la grille et un support linguistique étendu. Enfin, l'accompagnement des utilisateurs est assuré par la mise à jour des contenus pédagogiques de [grist-mooc](/repos/gristgouv/grist-mooc).

## Sécurité
- Intégration de l'analyseur de vulnérabilités Trivy pour sécuriser les images Docker dans [grist-docker-image](/repos/gristgouv/grist-docker-image).

## Autres changements notables
- Mise en conformité avec les standards d'accessibilité WCAG 2.1 AA pour le widget de vue groupée dans [grist-widget-grouped-view](/repos/gristgouv/grist-widget-grouped-view).
- Optimisation de l'infrastructure de conteneur via l'amélioration du workflow GVISOR dans [grist-docker-image](/repos/gristgouv/grist-docker-image).
- Amélioration de la gestion du trafic réseau par l'introduction du proxying Grist Fleet dans [grist-core](/repos/gristgouv/grist-core).
- Renforcement de la qualité logicielle par l'ajout de tests automatisés (smoke tests) dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).

## Dépôts les plus actifs
- [grist-widget-grouped-view](/repos/gristgouv/grist-widget-grouped-view) : Refonte majeure axée sur l'ergonomie, l'accessibilité et l'internationalisation.
- [grist-core](/repos/gristgouv/grist-core) : Évolutions de l'interface utilisateur et optimisations de l'infrastructure.
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Renforcement de la sécurité et optimisation des processus de construction.
- [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) : Amélioration de la robustesse de l'affichage et de la gestion des données.
- [widgets-config](/repos/gristgouv/widgets-config) : Extension de la bibliothèque de visualisation avec des widgets D3.js.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Actualisation des ressources et des exercices de formation.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Mise en place de tests automatisés pour la stabilité du code.
