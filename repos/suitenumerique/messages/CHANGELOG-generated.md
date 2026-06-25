## Changelog : messages (30 derniers jours, au 24 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la stabilité et de l'expérience utilisateur de Messages. Les principales évolutions concernent la gestion des brouillons, l'importation d'emails, la sécurité et l'interface utilisateur, avec une migration technique majeure vers de nouvelles technologies frontend (Vite et TanStack Router).

### Évolutions fonctionnelles
- **Brouillons :** Possibilité de supprimer définitivement les brouillons et amélioration de l'édition des brouillons.
- **Calendrier :** Ajout d'un lien vers une instance CalDAV pour accepter directement les événements.
- **Paramètres de la boîte de réception :** Regroupement des paramètres de la boîte de réception dans une boîte de dialogue dédiée.
- **Notifications :** Ajout de l'en-tête "To" aux emails sortants qui en étaient dépourvus.
- **Authentification :** Possibilité de créer une boîte de réception sans synchronisation d'identité.
- **Pièces jointes :** Prévisualisation des pièces jointes.
- **Interface utilisateur :** Amélioration de la navigation et de l'expérience utilisateur pour la sélection multiple de threads.
- **Langues :** Correction d'un problème de traduction automatique forcée par une configuration incorrecte.

### Évolutions techniques
- **Frontend :** Migration de Next.js vers Vite et TanStack Router pour une meilleure performance et une architecture plus moderne [#675](https://github.com/suitenumerique/messages/issues/675).
- **Bibliothèque d'emails :** Refactorisation du parser et du compositeur d'emails vers la nouvelle bibliothèque `jmap-email` [#700](https://github.com/suitenumerique/messages/issues/700).
- **Sécurité :** Renforcement de la sécurité de la connexion SMTP et des configurations de proxy. Ajout de mesures de défense en profondeur.
- **Dépendances :** Mise à jour de `django-lasuite` vers la version 0.0.27. Mise à jour de `keycloak` vers la version 26.6.3 [#718](https://github.com/suitenumerique/messages/issues/718). Mise à jour de `dompurify` vers la dernière version.
- **Architecture :** Suppression des champs de modèle dépréciés liés à la migration du stockage en niveaux.

### Autres changements
- Ajout de scripts de publication PyPI pour la bibliothèque `jmap-email`.
- Amélioration de la documentation et des tests.
- Correction de divers bugs et améliorations de la robustesse.
- Nouvelle illustration pour la page d'accueil [#702](https://github.com/suitenumerique/messages/issues/702).
- Internationalisation de chaînes de caractères manquantes.
- Correction de problèmes liés à la détection de fichiers Mbox.
- Correction de problèmes de permission de socket Milter au démarrage.
