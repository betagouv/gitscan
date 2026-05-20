## Changelog : st-transfers (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, l'équipe s'est concentrée sur l'amélioration de l'expérience utilisateur, notamment en optimisant l'interface mobile, en améliorant la gestion des transferts et des fichiers, et en intégrant une première version de la compatibilité avec des solutions de stockage en ligne comme Google Drive. Des efforts importants ont également été déployés pour nettoyer le code et améliorer la robustesse du service.

### Évolutions fonctionnelles
- **Téléchargement depuis S3 :** Optimisation du téléchargement de fichiers depuis S3 pour réduire la consommation de mémoire du navigateur.
- **Intégration Google Drive (WIP) :** Première implémentation de l'intégration avec Google Drive, permettant aux utilisateurs de transférer des fichiers depuis et vers cette plateforme. (en développement)
- **Amélioration de l'interface mobile :** Refonte de l'interface utilisateur sur mobile pour une meilleure expérience, incluant la correction de bugs et l'ajout d'un bouton de fermeture.
- **Gestion des transferts :**
    - Ajout d'un avertissement lors de la navigation hors d'un transfert en cours.
    - Amélioration de la fiabilité des téléchargements massifs.
    - Ajout d'un indicateur de progression et d'alertes lors du chargement de fichiers.
- **Notifications par email :** Refonte du système de notifications par email, avec ajout d'une option pour désactiver les notifications par défaut.
- **Choix de la durée de vie des liens :** Possibilité de configurer la durée de vie des liens de transfert, avec des valeurs par défaut ajustées.
- **Logo :** Mise à jour du logo de l'application.
- **Langue :** Ajout d'un sélecteur de langue dans l'interface de réception de fichiers.

### Évolutions techniques
- **Nettoyage du code :** Suppression de code obsolète, de dépendances inutilisées et de composants d'interface utilisateur non utilisés.
- **Refactoring backend :** Refactorisation de fonctions liées à la gestion des objets S3 et à la suppression des fichiers orphelins.
- **Gestion des erreurs S3 :** Amélioration de la gestion des erreurs lors des opérations S3, avec la possibilité de choisir d'ignorer ou de traiter les erreurs en fonction du contexte.
- **Tests :** Ajout de tests unitaires et fonctionnels pour améliorer la couverture et la robustesse du code.
- **Sécurité :** Renforcement de la sécurité en verrouillant les brouillons de transferts et en protégeant contre les attaques potentielles.
- **Pipeline d'envoi d'emails :** Amélioration du pipeline d'envoi d'emails pour une meilleure fiabilité et performance.
- **Utilisation de drafts :** Utilisation de brouillons pour les chargements de fichiers avant la création des transferts, améliorant ainsi l'expérience utilisateur.
- **Optimisation des performances :** Optimisation de la gestion de la mémoire pour les fichiers volumineux.

### Autres changements
- **Documentation :** Mise à jour de la documentation.
- **Linting :** Correction des erreurs de linting dans le code.
- **Configuration :** Ajout d'une option pour contourner l'authentification en développement.
- **Suppression de la langue néerlandaise :** Suppression du support de la langue néerlandaise.
- **Suppression de `Transfer.sensitive` :** Suppression du champ `sensitive` de la table `Transfer`.
- **Suppression des notifications par email pour l'agent de journalisation :** Suppression des notifications par email pour l'agent de journalisation.
