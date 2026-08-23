## Changelog : les-emplois (30 derniers jours, au 21 août 2026)

### Résumé
Ce mois a été marqué par le développement majeur du module d'**Insertion**, incluant la synchronisation des données avec l'outil Dora et de nouvelles interfaces de suivi. Nous avons également renforcé la **sécurité** via une gestion améliorée de la double authentification (2FA) et optimisé l'expérience de **gestion des candidats** grâce à des filtres plus précis et de meilleures performances d'affichage.

### Évolutions fonctionnelles
- **Module Insertion & Orientations** :
    - Mise en place de la synchronisation automatique des statuts depuis Dora.
    - Création de nouvelles vues de listes pour les orientations avec filtres avancés (par expéditeur, structure, statut ou bénéficiaire).
    - Ajout d'une commande d'importation des orientations via les fichiers d'export Dora.
- **Gestion des candidats (Job Seekers)** :
    - Ajout de nouveaux filtres de recherche (acteurs IAE, membres d'organisations, fin de parcours imminente).
    - Amélioration de la visibilité des informations de contact des conseillers.
    - Clarification de l'interface : affichage d'alertes lors de la mise à jour d'identités certifiées et explications sur les champs en lecture seule.
- **Processus de candidature** :
    - Amélioration de l'interface de saisie des dates de contrat et de recrutement avec des composants d'information contextuels.
    - Renforcement des contrôles de validation sur les dates de recrutement.
- **Sécurité & Authentification** :
    - Amélioration de l'expérience 2FA/OTP : ajout d'exemples d'applications d'authentification, d'un menu de configuration et de messages d'erreur plus explicites.
    - Renommage du composant `PoleEmploiConnect` (devenu `ft_connect`) pour une meilleure cohérence terminologique.
- **Expérience Utilisateur (UX)** :
    - Mise à jour des modèles d'emails (suppression des liens vers les enquêtes).
    - Mise en place d'une redirection automatique et d'un bandeau d'information lors du changement de domaine.

### Évolutions techniques
- **Refactoring & Architecture** :
    - Refonte majeure du composant `ft_connect` (renommage des modèles, tables et fonctions).
    - Implémentation de la "soft-deletion" (suppression logique) pour les services et les structures.
    - Refactorisation des vues de gestion des candidats pour une meilleure maintenabilité.
- **Performances** :
    - Optimisation des requêtes SQL (réduction des problèmes de type N+1) sur les listes de candidats et les recherches de conseillers.
- **Tests & CI/CD** :
    - Correction de tests instables (flaky tests) liés à Sentry.
    - Amélioration de la couverture de tests, notamment sur la sécurité et les redirections.
    - Mise à jour de la configuration CI/CD (setup-uv).

### Autres changements
- **Documentation** : Ajout de documentation concernant l'utilisation de Podman comme alternative à Docker sur Debian.
- **Maintenance** : Nettoyage général du code, suppression de templates et de tests inutilisés, et passage des commentaires techniques en anglais.
