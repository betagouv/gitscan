## Changelog : fce (30 derniers jours)

### Résumé
Cette version apporte une nouvelle fonctionnalité d'alerte de fermeture du portail, ainsi qu'une mise à jour de la liste des SIRET autorisés. Des corrections ont également été apportées pour améliorer la stabilité et la configuration du déploiement.

### Évolutions fonctionnelles
- Ajout d'une alerte de fermeture du portail (#381)
- Mise à jour de la liste des SIRET autorisés (#380)
- Activation du bouton Proconnect (#379)
- Intégration du bouton Proconnect (#374)

### Évolutions techniques
- Prévention du nettoyage de Strapi pendant le pré-déploiement (#383)
- Utilisation de `buildkit` dans GitHub Actions (#376)
- Utilisation de `cookieSession` pour la gestion des sessions (#373)
- Ajout de la variable d'environnement `proconnect prod secret` (#370, #369)
- Correction du chemin de configuration Nginx (#69b3dba)
- Correction de l'ID de processus Nginx (#a0233a7)

### Autres changements
- Publication de la version 27.114.0 (#2ab9d70)
