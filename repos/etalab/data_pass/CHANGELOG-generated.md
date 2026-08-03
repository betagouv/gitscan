## Changelog : data_pass (30 derniers jours, au 31 juillet 2026)

### Résumé
Les dernières mises à jour de data_pass se concentrent sur l'ajout de nouveaux éditeurs et formulaires (notamment pour DINUM et CNOUS), l'amélioration de l'expérience utilisateur (suppression de boutons inutiles, affichage d'emails automatisés), et la correction de bugs et vulnérabilités de sécurité. Des améliorations techniques ont également été apportées, notamment la mise à jour de dépendances et l'amélioration de la journalisation.

### Évolutions fonctionnelles
- Ajout de l'éditeur Hoptis Software et de ses formulaires API Particulier.
- Création du formulaire "Produits DINUM" (version 1) pour la gestion des habilitations.
- Intégration de la gestion de l'allocation de rentrée scolaire (CNOUS).
- Amélioration de la transmission de la convention aux contacts référents pour DINUM.
- Affichage des emails automatisés associés aux définitions d'habilitation.
- Suppression des boutons "Modifier" et du panneau latéral des formulaires d'instruction pour simplifier l'interface.
- Correction d'un bug empêchant la proactivité CNOUS pour les étudiants boursiers.
- Amélioration des wordings et des libellés pour une meilleure clarté.
- Ajout d'une page temporaire pour la gestion des emails.
- Ajout de breadcrumbs pour faciliter la navigation.
- Correction de la majuscule sur "DDmariage".
- Mise à jour des introductions pour les services CISIRH.

### Évolutions techniques
- Mise à jour de Rails à la version 8.1.3.1 pour corriger une vulnérabilité de sécurité (CVE-2026-66066).
- Suppression de la configuration d'environnement pour la production, le staging et le sandbox, désormais gérées par Ansible.
- Implémentation de la journalisation au format JSON via Logstasher.
- Mise à jour de plusieurs dépendances (oauth2, rails-html-sanitizer, actions/checkout, rubocop, css_parser, actions/cache).
- Suppression de l'ID d'autorisation France Connect lors de la suppression d'une modalité.
- Amélioration de la couverture de test pour les emails automatisés.

### Autres changements
- Documentation des tests pour les emails automatisés.
- Suppression du fichier `.keep` dans `tmp/storage/`.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de la suppression involontaire de droits lors d'un ajout.
- Ajout de tests unitaires et d'intégration.
- Refactorisation du code pour améliorer la maintenabilité.
- Uniformisation des cadres juridiques API Particulier.
- Masquage du téléphone et de la fonction des contacts Produits DINUM.
- Ajout d'un scope pour l'allocation de rentrée scolaire.
- Correction d'un bug lié à l'affichage de la date de transmission pour CNOUS.
