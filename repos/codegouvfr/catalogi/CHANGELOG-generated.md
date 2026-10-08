## Changelog : catalogi (30 derniers jours, au 07 octobre 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur le renforcement de la sécurité (notamment sur l'authentification et la prévention de certaines vulnérabilités), l'amélioration de l'expérience développeur via de nouveaux outils en ligne de commande et une meilleure documentation de l'API. L'interface utilisateur a également été affinée pour offrir un rendu plus propre.

### Évolutions fonctionnelles
- **Outils de gestion (CLI) :** Ajout de commandes en ligne de commande pour faciliter l'importation et la mise à jour des références [#577](https://github.com/codegouvfr/catalogi/issues/577).
- **API :** Mise à disposition d'une interface Swagger UI autonome pour documenter l'export public v2.
- **Interface utilisateur :** Amélioration de la clarté de la page d'accueil lorsqu'aucun cas d'usage n'est sélectionné et correction du logo.
- **Données :** Amélioration de la précision de l'identification des logiciels libres grâce à un meilleur ciblage des éléments Wikidata et des identifiants Zenodo.

### Évolutions techniques
- **Sécurité :** 
    - Correction d'une vulnérabilité liée à l'authentification OIDC (vuln-0008) en liant les transactions au navigateur initiateur.
    - Mise en place d'un environnement de test d'intrusion (pentest) local et éphémère.
    - Prévention des déclarations d'exécutables et des URLs d'instance.
- **API & Backend :**
    - Correction de la gestion des préfixes de documentation lors de l'utilisation de proxys.
    - Renforcement de la validation des schémas publics par rapport aux types de logiciels originaux.
    - Optimisation de la résolution des identifiants de projets GitLab [#575](https://github.com/codegouvfr/catalogi/issues/575).
- **Tests :** Amélioration significative de la couverture et de la structure des tests pour l'API et les configurations de l'interface utilisateur.

### Autres changements
- **Documentation :** Mise à jour de la documentation de déploiement suite à des revues de code.
- **Nettoyage :** Suppression de l'importation des anciennes configurations d'interface utilisateur lors des nouvelles installations pour simplifier le processus.
