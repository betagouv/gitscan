## Changelog : signalconso-website (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des catégories de signalements et la gestion des fichiers associés aux anomalies. La génération du flux d'actualités a été désactivée car elle n'était plus pertinente sans l'application mobile associée.

### Évolutions fonctionnelles
- Possibilité de sélectionner une entreprise étrangère lors du parcours de signalement Batrec [#1117](https://github.com/betagouv/signalconso-website/pull/1117).
- Modification du libellé des catégories de signalement [#1118](https://github.com/betagouv/signalconso-website/pull/1118).
- Suppression de "v1" de l'endpoint des catégories de signalement.

### Évolutions techniques
- Sanityzation manuelle des noms de fichiers des anomalies pour éviter les problèmes potentiels [#1117](https://github.com/betagouv/signalconso-website/pull/1117).
- Désactivation de la génération du flux d'actualités, jugée inutile sans l'application mobile.

### Autres changements
- Nettoyage et automatisation de la sanitization des noms de fichiers d'anomalies.
