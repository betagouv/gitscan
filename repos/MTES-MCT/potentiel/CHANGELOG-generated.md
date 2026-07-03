## Changelog : potentiel (30 derniers jours, au 2026-07-02)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment concernant la gestion des garanties financières, des raccordements et des candidatures. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Des optimisations techniques ont également été réalisées, notamment au niveau des scripts de restauration de base de données et des projections de données.

### Évolutions fonctionnelles
- Renommage de "démarches simplifiées" en "Démarche Numérique" pour plus de clarté. [#4403](https://github.com/MTES-MCT/potentiel/issues/4403)
- Amélioration de la redirection après une demande ou un passage en instruction de mainlevée. [#4412](https://github.com/MTES-MCT/potentiel/issues/4412)
- Affichage d'un bloc d'information pour les producteurs d'énergie avant de demander une mainlevée de garanties financières. [#4410](https://github.com/MTES-MCT/potentiel/issues/4410)
- Affichage du lien d'action sous le producteur et son identification. [#4407](https://github.com/MTES-MCT/potentiel/issues/4407)
- Correction des routes des candidatures. [#4404](https://github.com/MTES-MCT/potentiel/issues/4404)
- Possibilité de déselectionner une valeur dans un filtre multiple. [#4384](https://github.com/MTES-MCT/potentiel/issues/4384)
- Ajout de la possibilité de transmettre et modifier un document de raccordement. [#4385](https://github.com/MTES-MCT/potentiel/issues/4385)
- Affichage des données vérifiées dans la projection du détail de la candidature. [#4340](https://github.com/MTES-MCT/potentiel/issues/4340)
- Amélioration du wording concernant la date de mise en service. [#4397](https://github.com/MTES-MCT/potentiel/issues/4397)
- Affichage du motif de garantie financière en attente sur la page projet. [#4320](https://github.com/MTES-MCT/potentiel/issues/4320)
- Possibilité pour les producteurs de corriger leur numéro d'identification (SIRET/SIREN). [#4322](https://github.com/MTES-MCT/potentiel/issues/4322) et [#4317](https://github.com/MTES-MCT/potentiel/issues/4317)
- Ajout de l'opérateur "between" pour les exports lauréat et éliminés. [#4323](https://github.com/MTES-MCT/potentiel/issues/4323)
- Possibilité d'ouvrir un document sans le télécharger. [#4068](https://github.com/MTES-MCT/potentiel/issues/4068)
- Ajout de l'accès aux pages raccordement pour les GRD. [#4311](https://github.com/MTES-MCT/potentiel/issues/4311)
- Amélioration de la navigation au clavier du composant Multiselect (accessibilité). [#4346](https://github.com/MTES-MCT/potentiel/issues/4346)
- Amélioration de l'accessibilité des liens d'évitement. [#4350](https://github.com/MTES-MCT/potentiel/issues/4350)
- Ajout de labels ARIA sur les boutons "Copier" pour l'accessibilité. [#4387](https://github.com/MTES-MCT/potentiel/issues/4387)

### Évolutions techniques
- Rendre le script de restauration de base de données accessible aux review apps. [#4405](https://github.com/MTES-MCT/potentiel/issues/4405)
- Intégration des modifications des releases 3.80, 3.81, 3.82 et 3.83. [#4399](https://github.com/MTES-MCT/potentiel/issues/4399), [#4361](https://github.com/MTES-MCT/potentiel/issues/4361), [#4353](https://github.com/MTES-MCT/potentiel/issues/4353), [#4314](https://github.com/MTES-MCT/potentiel/issues/4314)
- Simplification du code et des composants, notamment au niveau des streams et des formulaires.
- Correction et amélioration des scripts de migration de base de données.
- Amélioration de la cohérence du stream d'achèvement. [#4307](https://github.com/MTES-MCT/potentiel/issues/4307)
- Utilisation des SHA1 des actions GitHub plutôt que des tags pour plus de sécurité. [#4310](https://github.com/MTES-MCT/potentiel/issues/4310)
- Correction des scripts DB et ajout du paramètre sslrootcert. [#4306](https://github.com/MTES-MCT/potentiel/issues/4306)
- Suppression de code obsolète (adapters, scripts de migration).

### Autres changements
- Correction de bugs mineurs et améliorations de la stabilité.
- Mise à jour des dépendances npm/yarn. [#4366](https://github.com/MTES-MCT/potentiel/issues/4366) et [#4365](https://github.com/MTES-MCT/potentiel/issues/4365)
- Amélioration de la documentation et des tests.
- Nettoyage du code et refactoring.
