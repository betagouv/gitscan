## Changelog : tchap-x-android (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment un renommage de "Tchap X" en "Tchap", des corrections de textes et de comportements, ainsi que l'ajout de fonctionnalités pour faciliter la navigation et la gestion des espaces. Des efforts ont également été faits pour améliorer la stabilité et la qualité du code.

### Évolutions fonctionnelles
- Renommage de l'application "Tchap X" en "Tchap" (plusieurs commits).
- Ajout d'un filtre des conversations par Espace directement depuis la liste des Espaces [#179](https://github.com/tchapgouv/tchap-x-android/pull/179).
- Affichage d'un message clair lorsque l'application Tchap est inaccessible.
- Correction de la description de l'onglet "Espace".
- Mise à jour de l'URL de signalement de bugs.
- Amélioration du surlignage des messages avec un dégradé corrigé.
- Alignement du wording avec la taxonomie Tchap (plusieurs commits).

### Évolutions techniques
- Mise à jour du format de version vers Major/Minor/Patch (temporaire).
- Script de génération de release pour Tchap implémenté [#179](https://github.com/tchapgouv/tchap-x-android/pull/179).
- Utilisation de `BuildTimeConfig` pour les variables publiques.
- Correction des jobs de build pour les tests Compose et l'analyse SonarCloud.
- Désactivation du "certificate pinning" pour les fonds de cartes et en environnement de développement.

### Autres changements
- Mise à jour des captures d'écran.
- Traduction des notes de release.
- Renommage des variants de build (devTchap & bTchap en tchapDev & tchapPreprod).
- Ajout d'un suffixe "beta" temporaire.
- Création du changelog pour les modifications Tchap.
