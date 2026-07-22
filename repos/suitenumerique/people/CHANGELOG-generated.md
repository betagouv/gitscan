## Changelog : people (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'intégration avec DiMail, permettant l'import automatique de boîtes aux lettres. Des corrections de sécurité ont également été implémentées, ainsi que des mises à jour de l'interface utilisateur et des scripts de publication.

### Évolutions fonctionnelles
- Possibilité d'importer automatiquement des boîtes aux lettres depuis DiMail. [#1040](https://github.com/suitenumerique/people/issues/1040)
- Augmentation du nombre d'utilisations maximales pour les codes de connexion DiMail, améliorant la flexibilité et la sécurité.
- Amélioration de l'importation des boîtes aux lettres depuis DiMail, notamment en utilisant la version 2 des boîtes aux lettres.
- Ajout d'une fonctionnalité pour rafraîchir les invitations expirées.
- Possibilité de supprimer les invitations aux domaines par un administrateur.
- Ajout de la gestion et de la suppression des alias. [#1002](https://github.com/suitenumerique/people/issues/1002)

### Évolutions techniques
- Mise à jour du script de publication pour inclure `uv`, améliorant la gestion des dépendances.
- Mise à jour des paquets `cryptography` et `tornado` pour renforcer la sécurité.
- Mise à jour de `PyJWT` vers la version 2.13.0 pour corriger une vulnérabilité de sécurité.
- Correction du Dockerfile pour réduire les vulnérabilités.
- Migration de `pip` vers `uv` pour la gestion des dépendances.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités (mjml, @html-to/text-cli, i18next-parser).

### Autres changements
- Mise à jour des chaînes de traduction pour l'internationalisation (i18n).
- Ajout d'une entrée au changelog pour le dernier commit.
- Correction d'un problème de slash final sur l'endpoint de vérification DiMail.
- Amélioration des messages d'erreur lors de l'importation des boîtes aux lettres.
- Correction de bugs mineurs liés à DiMail et aux invitations.
- Mise à jour de la configuration de l'interface utilisateur.
- Mise à jour du logo dans les modèles d'e-mails d'invitation.
- Utilisation du nouveau kit d'interface utilisateur Lasuite.
