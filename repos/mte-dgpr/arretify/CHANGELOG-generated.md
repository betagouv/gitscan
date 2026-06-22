## Changelog : arretify (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la détection des éléments structuraux des arrêtés, notamment les tableaux et les annexes.  La reconnaissance des adverbes multiplicatifs a également été améliorée, contribuant à une meilleure analyse du contenu. Des corrections de bugs et des optimisations ont été apportées pour une plus grande stabilité et fiabilité.

### Évolutions fonctionnelles
- **Détection des annexes :** Amélioration de la détection des "Prescriptions annexées" comme marqueur d'annexe. [#93](https://github.com/mte-dgpr/arretify/issues/93)
- **Détection des tableaux :**  Amélioration de la détection des sections de tableaux et correction des problèmes liés à la détection de tableaux uniques. [#78](https://github.com/mte-dgpr/arretify/issues/78)
- **Adverbes multiplicatifs :** Ajout de la détection des adverbes multiplicatifs dans les articles. [#81](https://github.com/mte-dgpr/arretify/issues/81)

### Évolutions techniques
- **CI/CD :** Correction de la configuration CI pour permettre le fallback vers le cache de développement en cas d'absence d'identifiants API.
- **Refactoring :** Renommage de "tableau" en "table" dans les identifiants pour une meilleure cohérence.
- **Correction de type d'erreur :** Correction d'un type d'erreur incorrect.

### Autres changements
- Suppression d'un test inutile.
- Mise à jour des snapshots après l'amélioration de la détection des prescriptions annexées.
- Corrections de formatage Black.
- Corrections mineures dans le code de détection des adverbes multiplicatifs.
