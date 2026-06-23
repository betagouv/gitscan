## Changelog : nosgestesclimat-app (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives sur l'expérience utilisateur, notamment concernant les actions proposées, le partage de résultats et l'intégration avec des outils externes. Des optimisations techniques ont également été apportées pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- **Actions :**
    - Amélioration du suivi des actions entreprises par les utilisateurs [#1830].
    - Affichage de l'impact des actions proposées [#1822].
    - Diverses améliorations de formulation et de présentation des actions [#1849, #1835, #1837].
    - Intégration des nouvelles actions synchronisées depuis Notion [#1812].
- **Partage et intégration :**
    - Ajout de support pour le partage de données via React Native WebView avec postMessage [#1828].
    - Correction du partage d'URL avec les paramètres UTM [#1821].
    - Possibilité de définir le mode simulation via l'URL [#1859].
- **Questionnaire et résultats :**
    - Implémentation d'une nouvelle question sur la tranche d'âge [#1788].
    - Amélioration de l'harmonisation des graphiques de catégories sur la page des résultats groupés [#1807].
    - Correction du comportement du bouton "Passer" pour la question d'âge [#1838].
    - Affichage du formulaire de contact en anglais [#1853].
    - Mise à jour du texte des services publics sur la page des résultats [#1851].
- **Divers :**
    - Correction d'un bug empêchant le chargement du modèle de nuit [#1860].
    - Amélioration de la visibilité et du SEO de la page de détails des actions [#1855].
    - Ajout d'un bouton pour déclencher manuellement le déploiement de l'application [#1834].

### Évolutions techniques
- **Architecture et performance :**
    - Utilisation de pnpm deploy au lieu de standalone pour la production [#1831].
    - Migration de zod vers valibot pour la validation des données [#1801].
    - Ajout d'un worker de calcul pour les actions [#1811].
- **Tests :**
    - Correction des tests E2E [#1836].
    - Ajout d'un helper `createPage` et d'une règle ESLint pour renforcer l'utilisation des feature flags dans les tests E2E [#1840].
- **Infrastructure :**
    - Ajout d'une migration pour les utilisateurs anonymes (AnonUser et AnonPoll) [#1856].
- **Autres :**
    - Remplacement de la librairie restcountries par un package npm [#1847].
    - Mise à jour de la version du modèle [#1810].
    - Correction d'un crash potentiel lié à la gestion des cookies en SSR [#1819].
    - Ajout de la gestion des variantes de feature flags (tests A/B) [#1816].

### Autres changements
- Suppression d'un lien mort [#1843].
- Correction d'un problème d'affichage d'iframes sur certaines versions de Safari [#1814].
- Amélioration du suivi automatique des événements, en ignorant les clics rapides et le simulateur [#1852].
- Mise à jour du titre de la page d'accueil [#1815, #1809].
- Amélioration du texte du mode étudiant [#1803].
- Ajout de la possibilité de masquer des éléments pour les intégrateurs utilisant des régions de modèle différentes [#1804].
