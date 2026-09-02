## Changelog : sylvasan (30 derniers jours, au 01 septembre 2026)

### Résumé
Ce mois-ci, sylvasan a bénéficié d'améliorations significatives pour faciliter la saisie de données sur le terrain, notamment via une meilleure gestion des formulaires et des images. La cartographie est devenue plus lisible grâce au regroupement de points (clustering), et les capacités d'exportation de données ont été enrichies pour offrir plus de contexte aux utilisateurs.

### Évolutions fonctionnelles
- **Saisie et formulaires** : 
    - Possibilité de réordonner les éléments au sein d'un champ de type liste (arrayfield) [#541](https://github.com/betagouv/sylvasan/pull/541).
    - Amélioration de la visibilité des champs obligatoires (labels, icônes et espacements) [#514](https://github.com/betagouv/sylvasan/pull/514).
    - Correction de l'affichage des résumés de formulaires contenant des images [#498](https://github.com/betagouv/sylvasan/pull/498).
- **Cartographie** : 
    - Ajout du clustering (regroupement de points) et intégration des suivis (*follow-ups*) directement sur la carte des observations [#515](https://github.com/betagouv/sylvasan/pull/515).
- **Gestion des images** : 
    - Correction de problèmes liés à la compression des images [#577](https://github.com/betagouv/sylvasan/pull/577).
    - Amélioration de l'affichage permettant de visualiser l'image complète [#498](https://github.com/betagouv/sylvasan/pull/498).
- **Exports** : 
    - Enrichissement des exports incluant désormais les suivis, le titre de l'enquête et les identifiants externes des répondants [#516](https://github.com/betagouv/sylvasan/pull/516).
- **Interface et UX** : 
    - Mise en place de filtres sur l'application mobile [#559](https://github.com/betagouv/sylvasan/pull/559).
    - Ajustement de l'interface Android pour intégrer l'espace des boutons de navigation [#542](https://github.com/betagouv/sylvasan/pull/542).
    - Sauvegarde automatique des données lors de la fermeture des fenêtres modales [#540](https://github.com/betagouv/sylvasan/pull/540).
    - Modification du libellé du bouton d'envoi d'enquête pour plus de clarté [#499](https://github.com/betagouv/sylvasan/pull/499).

### Évolutions techniques
- **Mobile** : Mises à jour de la version Android et des icônes de l'application.
- **Backend** : 
    - Optimisation du stockage des données en utilisant des identifiants plutôt que du format base64 pour les champs complexes.
    - Amélioration de la robustesse face aux conditions de concurrence (*race conditions*).
- **Frontend (Web)** : 
    - Mise à jour de la gestion de la navigation (Vue-router).
    - Résolution de problèmes de compatibilité entre les composants de l'interface (Pinia et Vue-dsfr).
- **Qualité et Tests** : 
    - Ajout de nouveaux tests et mise à jour des outils de contrôle de code (Ruff).

### Autres changements
- Mise à jour des mentions de licence pour le composant DSFR.
