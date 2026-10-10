## Changelog : catalogi (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilisation de l'importation des données et le renforcement de la sécurité de l'application. L'expérience utilisateur a été légèrement affinée avec une interface plus propre, tandis que de nouveaux outils en ligne de commande ont été introduits pour faciliter la gestion des références.

### Évolutions fonctionnelles
- **Interface utilisateur** :
  - Amélioration de la clarté de la page d'accueil lorsqu'aucun cas d'usage n'est sélectionné.
  - Correction de l'affichage du logo.

### Évolutions techniques
- **Importation et gestion des données** :
  - Amélioration de la précision de l'importation des logiciels via une meilleure gestion des identifiants (Zenodo, GitLab [#575], et CNLL).
  - Optimisation de la détection des licences de logiciels libres en utilisant les données Wikidata.
  - Correction de la gestion des doublons et des lignes non récupérées lors des processus d'import.
- **API et Sécurité** :
  - Renforcement de la sécurité de l'authentification OIDC en liant les transactions au navigateur initiateur.
  - Ajout d'une interface Swagger UI autonome pour documenter l'export public v2.
  - Sécurisation de l'API pour empêcher les déclarations d'exécutables et les URLs d'instance.
  - Correction de la gestion des préfixes de documentation lors de l'utilisation de proxys.
- **Outils et Développement** :
  - Introduction de nouvelles fonctionnalités en ligne de commande (CLI) pour l'importation et la mise à jour des références [#577].
  - Mise en place d'un environnement local dédié aux tests d'intrusion (pentest).
  - Amélioration de la robustesse des tests (validation des schémas API et détection des logiciels libres).

### Autres changements
- Mise à jour de la documentation de déploiement.
- Nettoyage du code et ajustements de style.
