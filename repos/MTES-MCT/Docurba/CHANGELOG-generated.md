## Changelog : Docurba (30 derniers jours, au 2 octobre 2026)

### Résumé
Ce mois-ci, Docurba a franchi des étapes importantes concernant l'expérience utilisateur et la sécurité. Les processus d'inscription, de vérification de compte et de réinitialisation de mot de passe ont été largement améliorés et sécurisés. Parallèlement, la plateforme renforce sa fiabilité métier avec de nouvelles règles de validation pour la création de procédures et une gestion plus robuste des données via un système d'archivage plutôt que de suppression.

### Évolutions fonctionnelles
- **Gestion des utilisateurs** : 
    - Réactivation de la création de comptes utilisateurs.
    - Amélioration du parcours d'inscription (gestion des erreurs de connexion, gestion des e-mails déjà existants et sécurisation des champs).
    - Mise en place de la réinitialisation globale des mots de passe.
    - Envoi automatique d'e-mails de vérification lors de la validation d'un profil.
- **Gestion des procédures** :
    - Affichage des dates d'approbation des procédures parentes dans les formulaires de procédures secondaires.
    - Nouvelles règles de blocage de la création de procédures pour garantir la cohérence des données (cas des communes absentes ou des configurations spécifiques EPCI).
    - Ajout du champ `name_complement` pour enrichir les données des procédures.
- **Administration** :
    - Amélioration de l'interface d'administration pour la gestion des projets partagés et la vérification des profils.

### Évolutions techniques
- **Sécurité et API** :
    - Migration des API vers Django Rest Framework (DRF) et passage des API en mode "privé par défaut".
    - Renforcement de la sécurité des données via l'ajustement des permissions Row Level Security (RLS).
    - Mise en place de mécanismes de "rate limiting" plus élevés pour prévenir les abus.
- **Intégrations tierces** :
    - Déploiement de l'intégration Sendgrid pour une gestion professionnelle et fiable des envois d'e-mails.
    - Intégration du client Pipedrive pour automatiser la vérification des utilisateurs.
- **Architecture et Maintenance** :
    - Nettoyage approfondi du frontend Nuxt (suppression du code mort et des endpoints API inutilisés).
    - Refactorisation de la structure du backend Django (réorganisation des applications et des dossiers exposés).
    - Transition d'une stratégie de suppression de données vers un système d'archivage des événements pour préserver l'historique.
    - Optimisation de la gestion des sessions utilisateurs pour éviter les durées infinies.

### Autres changements
- Ajout d'un fichier `security.txt` pour faciliter le signalement de vulnérabilités par les chercheurs en sécurité.
