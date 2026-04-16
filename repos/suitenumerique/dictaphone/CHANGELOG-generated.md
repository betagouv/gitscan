## Changelog : dictaphone (30 derniers jours, au 15 mai 2026)

### Résumé
Ce mois-ci, le projet Dictaphone a connu une évolution significative, notamment avec l'ajout d'une application mobile fonctionnelle (iOS et Android) permettant l'enregistrement, le téléchargement et la gestion des fichiers audio. L'interface web a également été grandement améliorée avec une nouvelle page d'accueil, une refonte des pages d'enregistrement et de listage des enregistrements, ainsi que l'ajout de fonctionnalités de corbeille et de suppression. L'intégration avec un service d'IA externe pour la transcription a été mise en place et améliorée.

### Évolutions fonctionnelles
- **Application Mobile :** Développement complet d'une application mobile (iOS et Android) avec les fonctionnalités suivantes :
    - Enregistrement audio
    - Téléchargement des enregistrements
    - Authentification utilisateur
    - Affichage de la liste des enregistrements
    - Suppression des enregistrements
- **Interface Web :**
    - Nouvelle page d'accueil avec une présentation standardisée. [#252f833](https://github.com/suitenumerique/dictaphone/commit/252f833)
    - Refonte complète des pages d'enregistrement et de listage des enregistrements avec une nouvelle interface utilisateur. [#4362afc](https://github.com/suitenumerique/dictaphone/commit/4362afc), [#5b38862](https://github.com/suitenumerique/dictaphone/commit/5b38862), [#ba53e69](https://github.com/suitenumerique/dictaphone/commit/ba53e69)
    - Ajout d'une fonctionnalité de corbeille permettant de supprimer et restaurer les enregistrements. [#019b1c5](https://github.com/suitenumerique/dictaphone/commit/019b1c5)
    - Possibilité de copier la transcription dans le presse-papier. [#0137418](https://github.com/suitenumerique/dictaphone/commit/0137418)
    - Affichage de la durée des enregistrements. [#4679bdd](https://github.com/suitenumerique/dictaphone/commit/4679bdd)
    - Ajout d'un badge "supprimé" pour les enregistrements supprimés. [#6796e2a](https://github.com/suitenumerique/dictaphone/commit/6796e2a)
- **Transcription :**
    - Intégration avec un service d'IA externe pour la transcription des enregistrements. [#342bc79](https://github.com/suitenumerique/dictaphone/commit/342bc79), [#633a581](https://github.com/suitenumerique/dictaphone/commit/633a581)
    - Affichage de la transcription et du résumé dans l'interface web. [#145845e](https://github.com/suitenumerique/dictaphone/commit/145845e)
- **Améliorations diverses :**
    - Amélioration de la réactivité de l'interface utilisateur. [#af50a42](https://github.com/suitenumerique/dictaphone/commit/af50a42), [#5bf0e13](https://github.com/suitenumerique/dictaphone/commit/5bf0e13)
    - Correction de bugs et amélioration de la stabilité. [#d3eb460](https://github.com/suitenumerique/dictaphone/commit/d3eb460), [#7021d65](https://github.com/suitenumerique/dictaphone/commit/7021d65)

### Évolutions techniques
- **Architecture :**
    - Intégration avec un service d'IA externe via une API.
    - Mise en place d'une redirection mobile pour l'application mobile. [#389857d](https://github.com/suitenumerique/dictaphone/commit/389857d)
- **Infrastructure :**
    - Mise à jour de la configuration Docker pour inclure les bibliothèques nécessaires. [#342bc79](https://github.com/suitenumerique/dictaphone/commit/342bc79)
    - Publication d'une première version Helm. [#d240726](https://github.com/suitenumerique/dictaphone/commit/d240726)
- **Backend :**
    - Amélioration de la gestion des permissions pour les jobs d'IA et les fichiers média. [#019b1c5](https://github.com/suitenumerique/dictaphone/commit/019b1c5)
    - Correction de bugs liés au support du format m4a. [#6fe742c](https://github.com/suitenumerique/dictaphone/commit/6fe742c), [#d3eb460](https://github.com/suitenumerique/dictaphone/commit/d3eb460)

### Autres changements
- Mise à jour de la documentation README pour une meilleure clarté. [#8e1c0a4](https://github.com/suitenumerique/dictaphone/commit/8e1c0a4)
- Amélioration de la configuration locale pour l'interface utilisateur. [#167edb4](https://github.com/suitenumerique/dictaphone/commit/167edb4)
- Corrections de labels de traduction. [#2c3ce06](https://github.com/suitenumerique/dictaphone/commit/2c3ce06)
- Amélioration de la gestion des jobs asynchrones. [#0070201](https://github.com/suitenumerique/dictaphone/commit/0070201)
