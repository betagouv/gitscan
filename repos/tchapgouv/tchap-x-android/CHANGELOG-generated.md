## Changelog : tchap-x-android (30 derniers jours, au 13 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment concernant la gestion des espaces et des salons, ainsi que des corrections de bugs et des ajustements de sécurité. L'application a été mise à jour avec la dernière version d'Element (26.03.3) et bénéficie d'améliorations visuelles et de corrections de l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout du filtre des conversations par Espace depuis la liste des Espaces.
- Possibilité de créer des salons privés non chiffrés.
- Ajout de l'option "Accès par lien" dans les paramètres du salon, facilitant l'invitation de nouveaux participants.
- Ajout de l'option "Limiter à mon domaine" pour les Salons publics, améliorant le contrôle de la visibilité.
- Renouvellement de l'invitation par email pour les futurs utilisateurs externes.
- Amélioration de l'expérience de vérification d'appareil : la saisie du code de vérification est désormais le premier écran.
- Alignement du wording avec la taxonomie Tchap pour une meilleure cohérence.

### Évolutions techniques
- Mise à jour du SDK Matrix Rust.
- Mise à jour des tokens de design compound pour une meilleure harmonisation visuelle.
- Utilisation de `BuildTimeConfig` pour les variables publiques, améliorant la configuration de l'application.
- Correction du job Compose tests lors du build.
- Correction du job Sonar lors du build.
- Désactivation du certificat pinning pour les fonds de cartes et sur l'environnement de développement.
- Suppression des délais inutiles lors de la récupération de `access_rules.visibility` via une requête.
- Import des `compound-design-tokens`.

### Autres changements
- Traduction des notes de release.
- Mise à jour de l'URL de report de bug.
- Correction de la couleur de texte des boutons secondaires.
- Nettoyage des options de sécurité & confidentialité.
- Mise à jour des screenshots.
- Versions : 0.6.0, 0.7.0, 0.8.0, 0.8.1, 0.8.2.
