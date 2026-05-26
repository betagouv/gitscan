## Changelog : grist-grav (30 derniers jours, au 21 mai 2026)

### Résumé
Cette mise à jour améliore la gestion des fichiers volumineux en désactivant les délais d'attente lors des uploads, ce qui permet d'utiliser Grist-Grav avec des fichiers plus importants. Des améliorations ont également été apportées à l'environnement de développement et au processus de construction pour une meilleure expérience des développeurs.

### Évolutions fonctionnelles
- Correction : Suppression des délais d'attente pour permettre l'upload de fichiers plus volumineux. [#3566332](https://github.com/betagouv/grist-grav/commit/3566332)
- Correction : Les fichiers sont maintenant conservés sur le disque après l'analyse, évitant ainsi des problèmes potentiels de perte de données. [#dac9efb](https://github.com/betagouv/grist-grav/commit/dac9efb)

### Évolutions techniques
- CI : La construction est maintenant effectuée pour toutes les branches, facilitant l'intégration continue et le test des modifications. [#8a04daf](https://github.com/betagouv/grist-grav/commit/8a04daf)
- Environnement de développement : Amélioration de la configuration de l'environnement de développement pour une meilleure expérience. [#8501d49](https://github.com/betagouv/grist-grav/commit/8501d49)
- Ajout de logs pour faciliter le débogage et la surveillance. [#102b2ab](https://github.com/betagouv/grist-grav/commit/102b2ab)
