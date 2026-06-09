## Changelog : nosgestesclimat (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de la précision des calculs (notamment pour les voyages en avion) et l'ajout de traductions. Des ajustements ont également été apportés pour répondre aux retours d'utilisateurs, notamment dans le contexte scolaire. Plusieurs versions mineures ont été publiées pour intégrer ces corrections et améliorations.

### Évolutions fonctionnelles
- Correction de la vitesse de calcul pour les voyages en avion, améliorant la précision de l'empreinte carbone estimée. [#2778](https://github.com/incubateur-ademe/nosgestesclimat/pull/2778)
- Amélioration des bornes de valeurs pour certains paramètres, pour une expérience utilisateur plus fluide. [#2767](https://github.com/incubateur-ademe/nosgestesclimat/pull/2767)
- Correction de l'affichage de la consommation DPE électrique. [#2768](https://github.com/incubateur-ademe/nosgestesclimat/pull/2768)
- Prise en compte des retours de Florence concernant le mode scolaire et le mode standard. [#2775](https://github.com/incubateur-ademe/nosgestesclimat/pull/2775)
- Ajout de traductions pour améliorer l'accessibilité du service. [#2771](https://github.com/incubateur-ademe/nosgestesclimat/pull/2771)

### Évolutions techniques
- Séparation du code frontend pour les trottinettes électriques, facilitant la maintenance et l'évolution de cette fonctionnalité. [#2772](https://github.com/incubateur-ademe/nosgestesclimat/pull/2772)
- Suppression de la dépendance `axios`.
- Plusieurs merges de branches `preprod` et `master` pour intégrer les corrections et les nouvelles fonctionnalités.

### Autres changements
- Publication des versions 4.12.0, 4.12.1, 4.12.2, 4.12.3, 4.12.4 et 4.12.5.
- Corrections de typographie et de formulation dans les traductions.
- Tests POC pour le mode scolaire. [#2740](https://github.com/incubateur-ademe/nosgestesclimat/pull/2740)
