## Changelog : demarche.numerique.gouv.fr (30 derniers jours, au 13 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de sécurité, notamment concernant la gestion des identités, des accès et la protection contre les vulnérabilités. Des optimisations de performance ont également été apportées, ainsi que des corrections de bugs et des améliorations de l'expérience utilisateur, notamment au niveau de la gestion des pièces justificatives et de l'interface administrateur. De nombreuses migrations techniques ont été réalisées pour moderniser le code et améliorer la maintenabilité.

### Évolutions fonctionnelles
- Amélioration de la gestion des pièces justificatives avec la possibilité d'uploader des fichiers .md et .xlsm.
- Ajout d'un indicateur visuel pour les champs de date préremplis avec FranceConnect.
- Possibilité de préremplir le champ date de naissance avec FranceConnect pour les usagers.
- Amélioration de la gestion des erreurs lors du téléchargement de fichiers.
- Ajout d'un système de notification pour les administrateurs avant l'expiration des tokens API Entreprise.
- Amélioration de la gestion des dossiers liés, notamment l'affichage de l'état (supprimé, expiré).
- Possibilité pour les administrateurs de personnaliser les colonnes affichées dans le tableau des dossiers pour les instructeurs.
- Ajout d'un bandeau d'information pour les administrateurs concernant le champ tableau.
- Amélioration de la gestion des batch operations (opérations en masse).
- Amélioration de l'affichage des informations sur les avis.

### Évolutions techniques
- Migration de nombreux composants Haml vers ERB pour une meilleure maintenabilité.
- Refactorisation du code pour améliorer la sécurité, notamment concernant la gestion des identités et des accès.
- Optimisation des performances de la recherche de dossiers.
- Migration des jobs de longue durée vers Sidekiq pour une meilleure gestion des erreurs et des retries.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour de plusieurs dépendances.
- Utilisation de Vips pour le traitement des images afin d'améliorer les performances.
- Amélioration de la gestion des caches.
- Refactorisation de la gestion des champs externes.
- Amélioration de la gestion des tests.
- Remplacement de l'authentification SAML.
- Utilisation de Tiptap pour les champs de texte dans le referentiel.

### Autres changements
- Documentation mise à jour.
- Correction de plusieurs erreurs de typographie et de grammaire.
- Amélioration de la couverture des tests.
- Suppression de code obsolète.
- Ajout de commentaires pour améliorer la lisibilité du code.
- Mise à jour des variables d'environnement.
- Amélioration de la configuration de l'environnement de développement.
