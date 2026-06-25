## Changelog : gristlabs-widgets (30 derniers jours, au 23 juin 2026)

### Résumé
Cette mise à jour améliore la robustesse et la lisibilité des widgets, notamment en gérant mieux l'affichage des erreurs et des données complexes. Les titres et les étiquettes des widgets sont désormais rendus en texte brut, évitant les problèmes potentiels liés à l'interprétation du HTML. Des corrections ont également été apportées pour assurer la compatibilité avec les dernières versions de Grist.

### Évolutions fonctionnelles
- Les erreurs et les messages d'inspection sont maintenant affichés en texte brut, améliorant la lisibilité et évitant les problèmes d'interprétation HTML. [#225](https://github.com/gristgouv/gristlabs-widgets/issues/225)
- Les étiquettes des widgets sont désormais rendues en texte brut au lieu de HTML, résolvant des problèmes d'affichage. [#221](https://github.com/gristgouv/gristlabs-widgets/issues/221)
- L'affichage des données JSON dans l'inspecteur est maintenant rendu en texte brut. [#229](https://github.com/gristgouv/gristlabs-widgets/issues/229)
- Le message "exoplanet greeting" dans l'inspecteur est également rendu en texte brut. [#227](https://github.com/gristgouv/gristlabs-widgets/issues/227)
- Amélioration de la sanitisation des titres pour éviter des problèmes d'affichage. [#223](https://github.com/gristgouv/gristlabs-widgets/issues/223)

### Évolutions techniques
- Mise à jour des tests pour assurer la compatibilité avec la dernière image de Grist. [#219](https://github.com/gristgouv/gristlabs-widgets/issues/219)
- Déplacement de toutes les dépendances de production vers les dépendances de développement. [#218](https://github.com/gristgouv/gristlabs-widgets/issues/218)

### Autres changements
- Mise à jour de la version du package à 0.0.7.
