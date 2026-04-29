## Changelog : tchap-x-android (30 derniers jours, au 24 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment une meilleure gestion des espaces, des corrections de bugs et des améliorations de l'interface. Des efforts ont également été faits pour faciliter le processus de publication de nouvelles versions et améliorer la robustesse de l'application.

### Évolutions fonctionnelles
- Ajout du filtre des conversations par Espace depuis la liste des Espaces.
- Affichage d'un message clair lorsque Tchap est inaccessible.
- Correction de la création des salons privés non chiffrés.
- Correction du dégradé pour le surlignage des messages.
- Amélioration de la description de l'onglet Espace.
- Alignement du wording avec la taxonomie Tchap [#2](https://github.com/tchapgouv/tchap-x-android/issues/2).
- Changement des couleurs de fond des messages et de l'UI contraste élevé.

### Évolutions techniques
- Mise à jour de l'URL de report de bug.
- Utilisation du `BuildTimeConfig` pour les variables publiques.
- Correction du job Compose tests lors du build.
- Correction du job SonarCloud lors du build.
- Désactivation du certificat pinning pour les fonds de cartes.
- Désactivation du certificate pinning sur l'environnement de développement.
- Mise à jour vers Element X 26.03.3 (f9024f5067).
- Script de génération de release pour Tchap [#179](https://github.com/tchapgouv/tchap-x-android/pull/179).
- Utilisation temporaire du format de version Major/Minor/Patch.
- Correction des délais inutiles lors de la récupération de `access_rules.visibility` via une requête.

### Autres changements
- Création du changelog pour les modifications Tchap.
- Correction de textes.
- Traduction des notes de release.
- Publication des versions 0.9.0, 0.8.2, 0.8.1 et 0.8.0, 0.7.0.
