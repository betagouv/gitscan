## Changelog : conversations (30 derniers jours, au 8 octobre 2026)

### Résumé
Ce mois-ci, Conversations s'enrichit de nouveaux outils de recherche et de génération de documents (web, data.gouv, présentations) tout en améliorant l'expérience utilisateur lors des mises à jour. Un effort majeur a été porté sur la protection de la vie privée en garantissant que les échanges des utilisateurs ne sont plus enregistrés dans les journaux système ni transmis à la télémétrie.

### Évolutions fonctionnelles
- **Nouveaux outils et connecteurs** : ajout de la recherche web (Staan), du connecteur data.gouv et d'un outil de génération de présentations (slide decks).
- **Amélioration de l'interface** : remplacement des actions de saisie par un nouveau menu déroulant "+" pour plus de clarté.
- **Expérience utilisateur et fiabilité** : 
    - Meilleure gestion des mises à jour avec une demande de rechargement de la page pour éviter l'utilisation de versions obsolètes.
    - Affichage d'une page d'erreur explicite au lieu d'une page blanche en cas de problème.
    - Possibilité pour l'utilisateur de forcer l'utilisation du connecteur data.gouv pour une interaction spécifique.
- **Correction** : support amélioré des fichiers Markdown dont le type MIME est manquant.

### Évolutions techniques
- **Confidentialité et sécurité** : renforcement de la protection des données en empêchant l'enregistrement des prompts utilisateurs dans les logs et la télémétrie.
- **Infrastructure et déploiement** :
    - Migration des tâches périodiques vers Celery Beat.
    - Optimisation de l'environnement de développement et de la CI en remplaçant MinIO par RustFS.
    - Sécurisation des ports de développement (limités à `localhost`).
- **Performance et stabilité** :
    - Optimisation de la lecture de la configuration pour réduire les entrées/sorties (I/O).
    - Réduction du bruit dans les logs (ASGI) et optimisation de la gestion des images CI.
- **Tests** : amélioration de la robustesse des tests frontend (mocking de composants et découplage des tests de langue).

### Autres changements
- **Documentation** : ajout de détails sur les procédures de release et de déploiement.
- **Internationalisation** : mise à jour des chaînes de caractères traduites [#769](https://github.com/suitenumerique/conversations/pull/769).
