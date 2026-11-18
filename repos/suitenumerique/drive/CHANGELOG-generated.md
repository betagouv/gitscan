## Changelog : drive (30 derniers jours, au 2026-11-17)

### Résumé
Cette période marque une étape majeure avec le passage à la version 1.0.0. Les utilisateurs bénéficient de fonctionnalités de partage nettement plus sécurisées grâce à l'ajout de mots de passe et de dates d'expiration sur les liens. La gestion des accès et des restrictions de dossiers a été considérablement affinée, tandis que l'interface a été améliorée pour offrir une meilleure accessibilité et une navigation plus claire.

### Évolutions fonctionnelles
- **Partage sécurisé** : Ajout de la possibilité de définir un mot de passe et une date d'expiration pour les liens de partage d'éléments.
- **Gestion des accès** : 
    - Possibilité de quitter un élément partagé [#826](https://github.com/suitenumerique/drive/issues/826).
    - Amélioration de la gestion des restrictions de dossiers (affichage dans le fil d'Ariane, gestion des descendants lors des suppressions ou déplacements).
    - Possibilité d'ouvrir la restriction d'un dossier à une liste spécifique d'utilisateurs.
- **Interface et Accessibilité** :
    - Amélioration de l'accessibilité (boutons d'icônes et en-têtes de listes nommés, titres de page dans le navigateur).
    - Ajout d'un accès direct au formulaire de support "La Suite" depuis le menu d'aide.
    - Amélioration de l'expérience utilisateur (infobulles pour les titres tronqués, sélection automatique du fichier après un upload).
- **Communications** : Refonte du design des emails (layout LaSuite) et possibilité de personnaliser le branding des emails via les paramètres.
- **Administration** : 
    - Nouvel outil d'importation des limites de stockage utilisateur via un fichier CSV.
    - Meilleure visibilité sur l'arborescence des fichiers et les accès depuis l'interface d'administration.

### Évolutions techniques
- **Observabilité et Métriques** : 
    - Intégration de métriques détaillées via Prometheus (métriques métier, état de la base de données, files d'attente Celery, ingress).
    - Mise en place de moniteurs de métriques dans les configurations Helm.
- **Performance** : 
    - Optimisation des calculs de métriques métier (utilisation d'index et calculs groupés).
    - Optimisation des recherches dans l'arborescence et de la gestion de la corbeille.
- **Sécurité et Infrastructure** :
    - Renforcement de la sécurité des uploads via des listes blanches (MIME types) et noires.
    - Durcissement de l'image de production (suppression de `pip` et mise à jour de l'image Python vers 3.13.17).
- **Logging** : Passage aux logs structurés au format JSON pour le backend afin de faciliter l'analyse.

### Autres changements
- **Documentation** : Mise à jour de la documentation concernant les métriques métier, les permissions du serveur de ressources, le partage et la configuration des emails.
