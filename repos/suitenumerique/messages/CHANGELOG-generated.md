## Changelog : messages (30 derniers jours, au 11 novembre 2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience mobile (iOS et Android) et une fiabilisation des processus d'importation de données (PST, IMAP, Google Drive). L'interface utilisateur a également été enrichie de nouveaux indicateurs visuels, notamment pour le suivi du stockage et la communication de messages de service.

### Évolutions fonctionnelles
- **Expérience Mobile :**
    - Amélioration de l'ergonomie : gestion optimisée du clavier sur iOS et Android, navigation par simple pression sur les dossiers/labels et barre d'outils de composition mieux positionnée.
    - Sécurité et notifications : ajout de l'aperçu chiffré des notifications sur mobile et correction de l'affichage du badge de messages non lus.
- **Gestion des données et imports :**
    - Optimisation de l'importation de contacts et messages depuis Outlook (PST) et IMAP (notamment pour les sous-dossiers Orange).
    - Amélioration de l'intégration Google Drive (détection de doublons par titre et déclaration de la taille des fichiers).
- **Interface et UX :**
    - Ajout de jauges de stockage pour les boîtes de réception et gestion de la purge des corbeilles/spams.
    - Introduction de bannières informatives pour les messages de service et l'état des réponses automatiques.
    - Pagination de la vue des métriques d'utilisation [#832].
    - Corrections diverses sur la fenêtre de composition, l'envoi des pièces jointes et l'affichage des fils de discussion.

### Évolutions techniques
- **Sécurité et Infrastructure :**
    - Renforcement de la sécurité des notifications push via un chiffrement des données pour l'appareil.
    - Mise à jour de l'environnement : passage à Python 3.14 [#821] et rafraîchissement des images Docker et des certificats CA [#829].
    - Sécurisation de la gestion des paramètres sensibles via l'utilisation de `SecretFileValue`.
- **Backend et Messagerie :**
    - Améliorations du protocole SMTP : journalisation des sessions [#844] et support de parties locales d'adresses plus longues (#853).
    - Ajout d'une commande d'exportation du corpus de spams vers un stockage objet.
- **Frontend et Tests :**
    - Refactoring du code frontend (utilisation de symboles privés JavaScript, gestion des tooltips via des portails).
    - Amélioration de la stabilité des tests de bout en bout (E2E) sur la CI.

### Autres changements
- Mise à jour de la documentation technique, notamment le README [#839] et les instructions relatives aux paramètres d'intégration Google Drive.
