## Changelog : meet-whisperx (30 derniers jours, au 02 juillet 2026)

### Résumé
Cette mise à jour améliore la stabilité de l'API en corrigeant une fuite de fichiers temporaires lors du chargement des fichiers audio. Elle met également à jour l'environnement d'exécution Python à la version 3.12 et les images Docker sous-jacentes pour bénéficier des dernières corrections et optimisations.

### Évolutions fonctionnelles
*   Correction d'un bug qui pouvait entraîner une fuite de fichiers temporaires lors du chargement des fichiers audio. [#46a15c7](https://github.com/suitenumerique/meet-whisperx/commit/46a15c7)

### Évolutions techniques
*   Mise à jour de la version minimale de Python requise à 3.12. [#d32eba0](https://github.com/suitenumerique/meet-whisperx/commit/d32eba0)
*   Mise à jour de l'image de base Docker pour bénéficier des dernières corrections et optimisations. [#34de05b](https://github.com/suitenumerique/meet-whisperx/commit/34de05b)
*   Suppression de l'utilisateur par défaut de l'image Docker de base pour une meilleure sécurité. [#1bd729b](https://github.com/suitenumerique/meet-whisperx/commit/1bd729b)
*   Mise à jour des dépendances non liées au GPU vers les dernières versions. [#5bfa9f9](https://github.com/suitenumerique/meet-whisperx/commit/5bfa9f9)
