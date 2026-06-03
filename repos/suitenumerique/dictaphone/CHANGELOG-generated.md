## Changelog : dictaphone (30 derniers jours, au 2026-06-02)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une interface utilisateur remaniée pour la liste des enregistrements et la page de lecture, ainsi que des corrections d'accessibilité.  Des améliorations ont également été apportées à l'application mobile, avec la prise en charge de nouveaux formats de fichiers, des corrections de bugs et des fonctionnalités de téléchargement améliorées.  Enfin, des corrections de sécurité et des optimisations internes ont été réalisées.

### Évolutions fonctionnelles
- **Interface utilisateur (Frontend):** Refonte de l'interface de la liste des enregistrements pour une meilleure lisibilité et ergonomie. [#6cc6254](https://github.com/suitenumerique/dictaphone/commit/6cc6254)
- **Interface utilisateur (Frontend):** Augmentation de la largeur de la liste des enregistrements pour afficher plus d'informations. [#779eba1](https://github.com/suitenumerique/dictaphone/commit/779eba1)
- **Interface utilisateur (Frontend):** Nettoyage et amélioration de l'interface de la page de lecture d'un enregistrement. [#efe3e71](https://github.com/suitenumerique/dictaphone/commit/efe3e71)
- **Interface utilisateur (Frontend):** Ajout d'un indicateur de durée maximale dans l'infobulle de téléchargement. [#f53fef5](https://github.com/suitenumerique/dictaphone/commit/f53fef5)
- **Interface utilisateur (Frontend):** Ajout de la possibilité de copier le texte de la transcription et d'ouvrir les documents associés. [#2252469](https://github.com/suitenumerique/dictaphone/commit/2252469)
- **Interface utilisateur (Frontend):** Ajout de l'exportation de transcriptions au format SRT. [#f49ee75](https://github.com/suitenumerique/dictaphone/commit/f49ee75)
- **Application Mobile:** Prise en charge de nouveaux formats audio/vidéo. [#fe272df](https://github.com/suitenumerique/dictaphone/commit/fe272df)
- **Application Mobile:** Possibilité de télécharger un fichier non uploadé. [#fe272df](https://github.com/suitenumerique/dictaphone/commit/fe272df)
- **Application Mobile:** Amélioration de l'expérience utilisateur lors du téléchargement, avec une barre de progression. [#10dcb1f](https://github.com/suitenumerique/dictaphone/commit/10dcb1f)
- **Application Mobile:** Ajout d'une option pour n'autoriser le téléchargement qu'en Wi-Fi. [#b350ff2](https://github.com/suitenumerique/dictaphone/commit/b350ff2)
- **Application Mobile:** Amélioration de la gestion des erreurs et des notifications. [#f36dc15](https://github.com/suitenumerique/dictaphone/commit/f36dc15)
- **Backend:** Ajout d'un endpoint pour relancer une génération de transcription en cas d'échec. [#fd9b751](https://github.com/suitenumerique/dictaphone/commit/fd9b751)
- **Backend:** Prise en charge de formats audio/vidéo plus variés. [#c19d9ce](https://github.com/suitenumerique/dictaphone/commit/c19d9ce)

### Évolutions techniques
- **Backend:** Mise à jour de Python vers la version 3.14.5 et de Django vers la version 5.12.4. [#c41aac4](https://github.com/suitenumerique/dictaphone/commit/c41aac4)
- **Frontend:** Amélioration de l'accessibilité de l'application web, avec des corrections d'attributs ARIA et de balises HTML. [#f427600](https://github.com/suitenumerique/dictaphone/commit/f427600) et autres commits liés.
- **Frontend:** Refactoring du composant `SignalLevelMeter` pour une meilleure performance et une visualisation plus fluide. [#0386260](https://github.com/suitenumerique/dictaphone/commit/0386260)
- **Backend:** Ajout d'une commande pour nettoyer les fichiers temporaires et supprimés. [#f270029](https://github.com/suitenumerique/dictaphone/commit/f270029)
- **Mobile:** Mise à jour de la librairie React Native Audio API. [#5b915ac](https://github.com/suitenumerique/dictaphone/commit/5b915ac)
- **Mobile:** Amélioration de la robustesse de la gestion des notifications sur iOS. [#f307f3c](https://github.com/suitenumerique/dictaphone/commit/f307f3c)
- **Sécurité:** Utilisation de `secrets.compare_digest` pour une comparaison de chaînes de caractères plus sécurisée. [#4e8ce56](https://github.com/suitenumerique/dictaphone/commit/4e8ce56)
- **Sécurité:** Mise à jour des dépendances avec des correctifs de sécurité (via Dependabot/Snyk). [#060cc31](https://github.com/suitenumerique/dictaphone/commit/060cc31), [#25cb521](https://github.com/suitenumerique/dictaphone/commit/25cb521), [#1fbdb00](https://github.com/suitenumerique/dictaphone/commit/1fbdb00), [#c673daf](https://github.com/suitenumerique/dictaphone/commit/c673daf), [#8ab4ab7](https://github.com/suitenumerique/dictaphone/commit/8ab4ab7)

### Autres changements
- **Documentation:** Mise à jour de la documentation pour l'utilisation locale en développement. [#d640ad9](https://github.com/suitenumerique/dictaphone/commit/d640ad9)
- **README:** Ajout d'un lien vers la salle Matrix du projet. [#75733f8](https://github.com/suitenumerique/dictaphone/commit/75733f8)
- **README:** Complétion du README pour la première release publique. [#2d7695d](https://github.com/suitenumerique/dictaphone/commit/2d7695d)
- Diverses corrections de bugs et améliorations de code.
- Mise à jour des dépendances.
