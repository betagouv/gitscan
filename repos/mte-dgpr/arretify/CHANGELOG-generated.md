## Changelog : arretify (30 derniers jours, au 19 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la détection des éléments structuraux des arrêtés, notamment la reconnaissance des tableaux et des prescriptions annexées. Des corrections et optimisations ont également été apportées pour améliorer la robustesse et la précision de la conversion des arrêtés en HTML.

### Évolutions fonctionnelles
- **Détection des tableaux :** Amélioration de la détection et de la gestion des tableaux présents dans les arrêtés, avec une identification plus précise des références aux tableaux [#78](https://github.com/mte-dgpr/arretify/issues/78).
- **Détection des prescriptions annexées :** Ajout de la détection des sections "Prescriptions annexées" et leur identification comme annexes [#93](https://github.com/mte-dgpr/arretify/issues/93).
- **Amélioration de la détection des adverbes multiplicatifs :**  Ajout de la détection des adverbes multiplicatifs dans les articles [#81](https://github.com/mte-dgpr/arretify/issues/81).

### Évolutions techniques
- **Correction d'erreurs de type :** Correction d'une erreur de type dans le code.
- **Optimisation du code de détection des adverbes multiplicatifs :** Petites corrections et optimisations du code lié à la détection des adverbes multiplicatifs.
- **Correction de la détection des sections de tableau uniques :** Correction d'un bug affectant la détection des sections de tableau uniques.
- **Amélioration de la CI :** Correction de la configuration de la CI pour permettre le fallback vers le cache de développement en cas d'absence d'identifiants API.
- **Refactoring :** Renommage de "tableau" en "table" dans les identifiants pour une meilleure cohérence.

### Autres changements
- **Suppression de test inutile :** Suppression d'un test jugé inutile.
- **Mise à jour des snapshots :** Mise à jour des snapshots après l'ajout de la détection des "Prescriptions annexées".
- **Corrections de formatage :** Corrections de formatage du code avec Black.
