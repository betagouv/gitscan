## Changelog : sill-deploy (30 derniers jours, au 08/11/2026)

### Résumé
Cette période a été marquée par une refonte de l'interface de consultation des logiciels pour la rendre plus fluide et intuitive, ainsi qu'une amélioration significative de la gestion automatique des sources de données. Les processus de déploiement et la sécurité de l'application ont également été renforcés pour garantir une meilleure stabilité et protection des informations.

### Évolutions fonctionnelles
- **Refonte de la page de détails des logiciels** : passage à un format "page unique" avec une navigation latérale pour faciliter la lecture et l'accès aux différentes sections.
- **Amélioration de l'ergonomie du formulaire** : la saisie de l'URL du dépôt est désormais demandée en priorité lors de la création d'un logiciel pour simplifier le processus.
- **Optimisation de l'affichage** : réorganisation de la section "usages" (incluant la participation) et alignement de l'interface sur les maquettes graphiques pour une meilleure cohérence visuelle.
- **Corrections d'interface** : résolution de problèmes de navigation interne et de liens d'ancrage sur la page de détails.

### Évolutions techniques
- **Gestion des sources et données** :
    - Automatisation de la création des sources (forges) à partir des identifiants de dépôts.
    - Amélioration de la gestion des priorités de sources et fusion des textes localisés pour les sources externes.
    - Ajout d'une fonctionnalité d'exportation des données au format Codemeta via un dump de la base de données.
- **Sécurité et API** :
    - Renforcement de la sécurité en limitant l'utilisation des dépôts au protocole HTTPS.
    - Restriction de l'accès aux configurations de sources sensibles, désormais masquées pour le navigateur.
    - Limitation de l'exploration des forges inconnues aux seuls administrateurs.
- **Infrastructure et CI/CD** :
    - Mise en place de nouveaux workflows de déploiement et de configurations de personnalisation.
    - Mise à jour des environnements de test (Playwright) pour assurer la compatibilité avec les dernières versions d'Ubuntu.
    - Verrouillage de la version Node.js pour garantir la stabilité et la sécurité.
- **Tests** :
    - Mise à jour complète des tests de bout en bout (E2E) pour accompagner les changements structurels de l'interface et des données.

### Autres changements
- **Documentation** : ajout de la documentation concernant les identifiants (credentials) des forges.
- **Maintenance** : ajout d'un script de peuplement de la base de données (`db:seed`) pour faciliter les environnements de développement.
