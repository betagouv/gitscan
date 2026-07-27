## Changelog : meet-whisperx (30 derniers jours, au 02 juillet 2026)

### Résumé
Cette mise à jour améliore la stabilité et la sécurité de l'API, notamment en corrigeant une potentielle fuite de fichiers temporaires lors du chargement des fichiers audio.  Elle met également à jour les dépendances et l'image Docker de base pour bénéficier des dernières corrections et optimisations.

### Évolutions fonctionnelles
Aucune évolution fonctionnelle majeure n'a été apportée durant cette période.

### Évolutions techniques
- Correction d'une fuite de fichiers temporaires lors du chargement des fichiers audio [#46a15c7](https://github.com/suitenumerique/meet-whisperx/commit/46a15c7).
- Mise à jour de la version minimale de Python requise à 3.12 [#d32eba0](https://github.com/suitenumerique/meet-whisperx/commit/d32eba0).
- Mise à jour de l'image de base Docker utilisée pour l'application [#34de05b](https://github.com/suitenumerique/meet-whisperx/commit/34de05b).
- Suppression de l'utilisateur par défaut de l'image Docker de base pour renforcer la sécurité [#1bd729b](https://github.com/suitenumerique/meet-whisperx/commit/1bd729b).
- Mise à jour des dépendances non liées au GPU vers les dernières versions [#5bfa9f9](https://github.com/suitenumerique/meet-whisperx/commit/5bfa9f9).

### Autres changements
Aucun autre changement significatif à signaler.
