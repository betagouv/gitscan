## Changelog : dossierfacile-backend (30 derniers jours, au 13 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées au backend de DossierFacile.fr au cours des 30 derniers jours. Les évolutions concernent principalement l'interface d'administration (back-office) avec de nouvelles fonctionnalités pour la gestion des documents et des applications, ainsi que des corrections et améliorations de l'API et de la logique métier. Des optimisations ont également été apportées à la validation des justificatifs de revenus.

### Évolutions fonctionnelles
- **Back-office :** Possibilité de supprimer un fichier individuel directement depuis la page de l'application [#1222].
- **Back-office :** Augmentation de la limite d'actions de recherche [#1228].
- **Back-office :** Ajout d'un tableau des temps d'attente pour le rôle de gestionnaire [#1224].
- **Back-office :** Le commentaire de l'opérateur est maintenant conservé lors du traitement d'un fichier [#1223].
- **Back-office :** Affichage des métadonnées des fichiers sur la page de l'application [#1221].
- **Garantie :** Ajout de la possibilité de spécifier un nom préféré pour le garant [#1227].
- **Justificatifs de revenus :** Restriction de la validation des fiches de paie aux cas de salaire de plus de 3 mois [#1235].
- **Logique métier :** Correction de la logique `honorDeclaration` pour les couples [#1229].
- **API :** Correction d'un bug concernant le format de la date retournée par l'API ADEME.
- **API :** Correction pour utiliser l'ID du locataire impacté lors de la suppression d'un couple de documents [#1232].
- **Document IA :** Correction du type de retour lorsque le document IA est inconnu [#1237].
- **BO :** Appel à la prévisualisation des fichiers uniquement lorsque nécessaire [#1236].

### Évolutions techniques
- **Feature Flags :** Correction de la gestion de la date de déploiement des feature flags [#1231].
- **Analyse :** Ajout d'une nouvelle règle d'analyse pour le numéro de page des impôts [#1225].
- **Date Tenant :** Mise à jour de la date de dernière modification du locataire [#1219].
- **Anonymisation :** Suppression de la colonne `json_profile` de la table `tenant_log` pour l'anonymisation [#1238].

### Autres changements
- Mise à jour des dépendances du projet [#1233].
- Préparation des versions 3.5.6, 3.5.7 et 3.5.8.
