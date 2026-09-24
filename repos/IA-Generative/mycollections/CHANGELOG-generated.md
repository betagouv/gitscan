## Changelog : mycollections (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois a marqué une étape majeure avec l'ouverture de la plateforme à la communauté. L'outil devient collaboratif : les utilisateurs peuvent désormais soumettre des demandes, proposer des améliorations et suivre l'avancement des travaux via un nouveau système de suivi. L'expérience de recherche a également été grandement simplifiée pour rendre les sources des réponses de l'IA plus lisibles, transparentes et faciles d'accès.

### Évolutions fonctionnelles
- **Engagement communautaire (Collectif) :** Mise en place d'un système complet pour que les utilisateurs deviennent acteurs : gestion des demandes, parcours d'états, propositions, signalements et fil d'actualité. [#10](https://github.com/IA-Generative/mycollections/pull/10)
- **Nouveaux connecteurs de données (Amorces) :** Intégration de six nouveaux connecteurs (NATINF, SSMSI, justice administrative, RNE, SIS, BAAC) permettant l'importation automatique de jeux de documents. [#9](https://github.com/IA-Generative/mycollections/pull/9)
- **Amélioration de l'expérience de recherche (Playground) :** 
    - Les sources des réponses sont désormais présentées de manière structurée (titres, extraits) plutôt qu'en listes brutes. [#15](https://github.com/IA-Generative/mycollections/pull/15)
    - Les liens vers les documents passent désormais par un proxy pour éviter les erreurs d'accès. [#14](https://github.com/IA-Generative/mycollections/pull/14)
    - Amélioration de la visibilité des bulles de sources et des extraits de texte. [#27](https://github.com/IA-Generative/mycollections/pull/27)
- **Gestion des collections et du catalogue :**
    - **Visualisation :** Le graphe de documents est désormais plus ergonomique (mode plein écran, import de graphes externes, filtres par livre). [#19](https://github.com/IA-Generative/mycollections/pull/19) [#36](https://github.com/IA-Generative/mycollections/pull/36)
    - **Fiches :** Ajout d'onglets pour consulter le corpus, amélioration de la lisibilité des publications et ajout d'un guide sur "où interroger la collection". [#33](https://github.com/IA-Generative/mycollections/pull/33) [#16](https://github.com/IA-Generative/mycollections/pull/16)
    - **Catalogue :** Interface plus fluide avec des animations de chargement et une meilleure distinction visuelle des catégories. [#39](https://github.com/IA-Generative/mycollections/pull/39) [#40](https://github.com/IA-Generative/mycollections/pull/40)
- **Contrôle de publication :** Renforcement des droits pour publier, archiver ou supprimer des collections, avec des confirmations de sécurité. [#34](https://github.com/IA-Generative/mycollections/pull/34)

### Évolutions techniques
- **Authentification et Sécurité :** 
    - Amélioration de la gestion des accès par groupe et résolution des problèmes d'identité. [#3](https://github.com/IA-Generative/mycollections/pull/3)
    - Sécurisation des scripts en supprimant la présence de mots de passe en clair.
- **Architecture et Intégration :**
    - Connexion au "bus" de la bêta pour la synchronisation des événements (demandes, suivi, notifications). [#11](https://github.com/IA-Generative/mycollections/pull/11)
    - Intégration d'un menu commun et harmonisation du flux d'authentification. [#11](https://github.com/IA-Generative/mycollections/pull/11)
- **Indexation et Traitement :** 
    - Optimisation de l'indexation pour que chaque fragment de texte conserve précisément son origine (titre du document, section, nom de fichier). [#13](https://github.com/IA-Generative/mycollections/pull/13)
    - Correction du processus de découpage des documents (chunking) pour éviter les erreurs en fin de fichier. [#1](https://github.com/IA-Generative/mycollections/pull/1)

### Autres changements
- **Documentation :** Mise à jour du README et rédaction de procédures de déploiement neutres et paramétrables. [#29](https://github.com/IA-Generative/mycollections/pull/29) [#31](https://github.com/IA-Generative/mycollections/pull/31)
