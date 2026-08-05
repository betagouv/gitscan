## Changelog : maestro (30 derniers jours, au 04/08/2026)

### Résumé
Les récentes évolutions de Maestro se concentrent sur l'enrichissement du tableau de bord (statistiques et cartographie) et l'optimisation des processus de gestion des prélèvements. Des améliorations significatives ont été apportées à la précision des données d'analyse et à l'ergonomie des interfaces de saisie, tout en optimisant la consommation de ressources du système.

### Évolutions fonctionnelles
- **Tableau de bord** : Ajout de nouvelles statistiques [#949], correction de l'affichage des cartes [#1179] et fiabilisation des calculs de pourcentages (exclusion des éléments non recevables) [#1188, #1189, #1262].
- **Gestion des prélèvements et échantillons** : 
    - Ajout d'un filtre sur la date d'envoi de la DAI [#1231].
    - Mise en place d'une saisie semi-automatique (autocomplete) pour la sélection des laboratoires [#1196].
    - Amélioration de la visibilité des prélèvements régionaux pour les coordinateurs [#1184].
    - Correction de la déduction automatique du type de destinataire pour les exemplaires de prélèvements [#1186].
    - Amélioration de l'ergonomie avec l'ouverture par défaut des détails d'un échantillon [#1229].
- **Analyses et Référentiel** : 
    - Ajout d'une nouvelle méthode d'analyse pour Girpa [#1265].
    - Intégration de la substance active cyprosulfamide dans le référentiel [#1246].
    - Améliorations et corrections sur les modules Cereco [#1264, #1183], Labcam [#1213] et la gestion des RAI DAOA [#1149].
- **Interface et exports** : 
    - Correction de l'affichage des noms de documents dans les tableaux [#1232].
    - Nettoyage de la gestion des espaces dans les références [#1263].
    - Correction des décalages de lignes dans les exports de programmation [#1185].
    - Correction de la vue nationale du tableau de programmation [#1155].

### Évolutions techniques
- **Performance et ressources** : Optimisation de la consommation de mémoire vive (RAM) en passant la mise à jour des départements en mode non automatique [#1260].
- **Architecture et sécurité** : 
    - Ajout de la politique de sécurité de contenu (CSP) pour Sentry [#1176].
    - Correction d'erreurs de validation dans la console liées à Zod [#1177].
    - Unification du code utilisé pour l'extraction des références Maestro dans les laboratoires [#1247].
- **Build et infrastructure** : 
    - Amélioration du processus de nettoyage des sauvegardes (restic).
    - Suppression des avertissements (warnings) lors du build Vite [#1261].
    - Migration de l'outil de gestion de scripts vers `npm-run-all2` [#1243].

### Autres changements
- **Maintenance** : Mises à jour régulières des outils de développement et de l'environnement de travail (TypeScript, Vitest, Storybook, etc.).
