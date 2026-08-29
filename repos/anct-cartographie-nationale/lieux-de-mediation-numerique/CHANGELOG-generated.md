## Changelog : lieux-de-mediation-numerique (30 derniers jours, au 28/08/2026)

### Résumé
Cette mise à jour introduit des capacités de déduplication pour identifier et gérer les doublons de lieux, améliorant ainsi la qualité des données traitées. Une modification majeure de la logique de traitement a été introduite, ce qui peut nécessiter des ajustements de la part des développeurs utilisant la bibliothèque.

### Évolutions fonctionnelles
- Implémentation d'une règle de déduplication des lieux [#66](https://github.com/anct-cartographie-nationale/lieux-de-mediation-numerique/pull/66), [#69](https://github.com/anct-cartographie-nationale/lieux-de-mediation-numerique/pull/69).
- Correction de la logique de distinction entre deux noms pour affiner la détection des doublons [#73](https://github.com/anct-cartographie-nationale/lieux-de-mediation-numerique/pull/73).

### Évolutions techniques
- **Changement majeur (Breaking Change) :** Refonte du processus de déduplication pour optimiser la préparation des lieux et la validation des paires [#71](https://github.com/anct-cartographie-nationale/lieux-de-mediation-numerique/pull/71).
- Sécurisation de la publication sur npm via le mécanisme "trusted publishing" [#70](https://github.com/anct-cartographie-nationale/lieux-de-mediation-numerique/pull/70).
- Amélioration de la CI pour la reconnaissance automatique des changements majeurs (breaking changes) [#72](https://github.com/anct-cartographie-nationale/lieux-de-mediation-numerique/pull/72).
