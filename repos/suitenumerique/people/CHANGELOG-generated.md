## Changelog : people (30 derniers jours, au 24 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'intégration avec DiMail, permettant notamment l'import automatique de boîtes aux lettres. Des corrections de sécurité ont également été implémentées, ainsi que des mises à jour de l'interface utilisateur et des scripts de publication.

### Évolutions fonctionnelles
- Possibilité d'importer automatiquement les boîtes aux lettres depuis DiMail. [#1040](https://github.com/suitenumerique/people/issues/1040)
- Augmentation du nombre d'utilisations maximales pour les codes de connexion DiMail afin d'améliorer la flexibilité.
- Amélioration de l'importation des boîtes aux lettres depuis DiMail, notamment en utilisant la version V2 des boîtes aux lettres.
- Ajout d'une fonctionnalité permettant de rafraîchir les invitations expirées.
- Possibilité de supprimer les invitations d'accès aux domaines par un administrateur.
- Ajout d'une interface pour afficher et supprimer les invitations d'accès aux domaines.
- Gestion des alias : création, suppression et administration des alias. [#1002](https://github.com/suitenumerique/people/issues/1002)
- Possibilité de supprimer toutes les alias en une seule opération. [#1002](https://github.com/suitenumerique/people/issues/1002)

### Évolutions techniques
- Mise à jour du script de publication pour inclure l'outil `uv`.
- Mise à jour des paquets `cryptography` et `tornado` pour améliorer la sécurité.
- Mise à jour de la dépendance `PyJWT` vers la version 2.13.0 pour corriger une vulnérabilité de sécurité.
- Correction du Dockerfile pour réduire les vulnérabilités.
- Migration de l'utilisation de `pip` vers `uv` pour la gestion des dépendances.
- Correction d'une vulnérabilité en mettant à jour la version de Python. [#1010](https://github.com/suitenumerique/people/issues/1010)

### Autres changements
- Mise à jour des chaînes de traduction pour l'internationalisation (i18n).
- Publication de la version 1.26.0.
- Ajout d'une entrée au changelog pour le dernier commit.
- Correction d'un problème de slash final sur l'endpoint de vérification DiMail.
- Amélioration du message d'erreur lorsque l'adresse e-mail secondaire n'est pas disponible.
- Correction de l'envoi de codes de connexion DiMail à l'URL incorrecte.
- Mise à jour des dépendances `mjml` et `@html-to/text-cli`.
- Mise à jour de la dépendance `i18next-parser` pour corriger des vulnérabilités.
