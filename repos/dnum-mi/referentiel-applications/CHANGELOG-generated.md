## Changelog : referentiel-applications (30 derniers jours, au 04 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives en termes d'accessibilité (RGAA), d'import de données (Excel, MAIA) et de fonctionnalités d'administration (gestion des droits, impersonation). Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- **Import de données :**
    - Ajout de l'import d'acteurs depuis un fichier Excel [#751](https://github.com/dnum-mi/referentiel-applications/issues/751)
    - Import Excel des onglets applications et hébergements [#752](https://github.com/dnum-mi/referentiel-applications/issues/752)
    - Import Excel avec gestion des conformités [#1881](https://github.com/dnum-mi/referentiel-applications/issues/1881)
- **Administration :**
    - Possibilité de modifier globalement les applications en tant qu'administrateur [#1888](https://github.com/dnum-mi/referentiel-applications/issues/1888)
    - Implémentation de l'impersonation d'un utilisateur par un administrateur [#1764](https://github.com/dnum-mi/referentiel-applications/issues/1764)
- **Recherche :**
    - Mise en place d'une recherche plein texte des applications [#1753](https://github.com/dnum-mi/referentiel-applications/issues/1753)
- **MDIT :**
    - Ajout de la gestion des millésimes MDIT (campagnes dette IT) avec sélecteur de période et accès administrateur [#1848](https://github.com/dnum-mi/referentiel-applications/issues/1848)
- **MAIA :**
    - Intégration de l'import MAIA dans le formulaire d'acteur [#1762](https://github.com/dnum-mi/referentiel-applications/issues/1762)
    - Vérification de l'email MAIA lors de la modification d'un utilisateur [#1818](https://github.com/dnum-mi/referentiel-applications/issues/1818)
    - Gestion des organisations MAIA lors de la création d'un utilisateur [#1793](https://github.com/dnum-mi/referentiel-applications/issues/1793)
- **Filtres :**
    - Ajout de filtres de conformité et mise à jour des composants associés [#1788](https://github.com/dnum-mi/referentiel-applications/issues/1788)

### Évolutions techniques
- **Accessibilité (RGAA) :**
    - Amélioration de l'accessibilité de plusieurs composants (combobox, autocomplete, étiquettes de champs, gestion du focus, etc.) pour répondre aux critères RGAA.
- **Sécurité :**
    - Résolution des alertes de sécurité détectées par CodeQL [#1846](https://github.com/dnum-mi/referentiel-applications/issues/1846)
- **Infrastructure :**
    - Correction pour permettre l'écriture de l'image frontend dans un environnement OpenShift [#1914](https://github.com/dnum-mi/referentiel-applications/issues/1914)
- **Tests :**
    - Ajout de tests de non-régression (e2e) pour plusieurs domaines fonctionnels.
- **Refactoring :**
    - Correction de code smells TypeScript détectés par SonarQube [#1898](https://github.com/dnum-mi/referentiel-applications/issues/1898)
    - Amélioration de la gestion des erreurs et des promesses.
- **CI/CD :**
    - Publication des versions 1.80.1 et 1.80.0.

### Autres changements
- Mise à jour de la configuration des tests unitaires frontend.
- Suppression du plugin vite-plugin-vue-devtools.
- Correction de la valeur totale pour le MDIT.
- Amélioration de la représentation graphique du MDIT.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de la validation par défaut dans la page de recherche d'applications.
- Possibilité de rendre la date de statut optionnelle.
- Ajout de la gestion des groupes MAIA/MOE lors de la création d'une application.
- Correction de l'affichage des valeurs dans le graphique iqchart.
- Mise à jour des URLs Swagger OIDC.
- Correction d'un bug lié à la gestion des permissions.
- Ajout d'une fonction de comparaison pour les tris de tableaux.
- Correction de l'affichage des libellés "Maîtrise des coûts".
- Suppression des permissions d'écriture globales sur l'image frontend.
- Correction de l'emplacement du titre "Détails de la modification" dans les tests e2e.
- Mise à jour de la table refapp avec le tri.
- Ajout de la possibilité de tracer les modifications de la matrice des droits dans l'historique de refapp.
