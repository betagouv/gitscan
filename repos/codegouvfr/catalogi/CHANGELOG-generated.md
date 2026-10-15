## Changelog : catalogi (30 derniers jours, au 12 octobre 2026)

### Résumé
Les récentes évolutions de Catalogi se concentrent sur l'amélioration de l'importation de données, l'ajout d'outils de gestion en ligne de commande et le renforcement de la sécurité. L'expérience utilisateur est également affinée avec une interface plus propre et une meilleure documentation de l'API.

### Évolutions fonctionnelles
- **Outils d'administration** : Ajout de commandes en ligne de commande pour faciliter l'importation et la mise à jour des références [#577](https://github.com/codegouvfr/catalogi/issues/577).
- **Export de données** : Nouvelle possibilité d'exporter les données Codemeta sous forme de dump de la base de données.
- **Documentation API** : Mise à disposition d'une interface Swagger UI autonome pour documenter l'export public v2.
- **Interface utilisateur** : Amélioration de la clarté de la page d'accueil (lorsqu'aucun cas d'usage n'est présent) et correction du logo.

### Évolutions techniques
- **Sécurité** : Correction d'une vulnérabilité liée à la liaison des transactions de connexion OIDC au navigateur initiateur (vuln-0008) et création d'un environnement de test d'intrusion (pentest) local.
- **Gestion des données et imports** : 
    - Optimisation des processus d'importation (gestion des identifiants Zenodo, suppression des doublons et amélioration de la correspondance CNLL).
    - Affinement de la détection des licences de logiciels libres via Wikidata.
- **API & Backend** : 
    - Amélioration de la gestion des préfixes de documentation derrière les proxys.
    - Renforcement de la validation des schémas publics par rapport aux types de logiciels originaux.
    - Correction de la résolution des identifiants de projets GitLab [#575](https://github.com/codegouvfr/catalogi/issues/575).
- **Tests et Qualité** : Amélioration de la couverture de tests pour l'API (validation des schémas sans serveur HTTP) et mise à jour des tests relatifs aux licences libres.

### Autres changements
- **Documentation** : Mise à jour de la documentation de déploiement.
- **Configuration** : Suppression de l'importation des configurations d'interface utilisateur obsolètes lors des nouvelles installations.
- **Maintenance** : Nettoyage du code (style) et refactorisation du système de journalisation (timelog).
