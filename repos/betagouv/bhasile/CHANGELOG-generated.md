## Changelog : bhasile (30 derniers jours, au 11 septembre 2026)

### Résumé
Cette période est marquée par un renforcement des capacités d'extraction de données (exports Excel et PDF) et une amélioration de l'expérience utilisateur via de nouveaux éléments d'accessibilité et des corrections d'interface. En coulisses, le projet bénéficie d'une modernisation technique importante pour optimiser le chargement des données grâce aux composants serveurs de React.

### Évolutions fonctionnelles
- **Exportation de données** : Ajout de nouvelles options d'exportation, notamment en format Excel pour les statistiques [#1640], via une nouvelle modale PDF [#1632], ainsi que l'ajout de téléchargements de feuilles de calcul supplémentaires [#1625] et l'export des types de lieux [#1614].
- **Expérience utilisateur et accessibilité** : Création d'une page dédiée à l'accessibilité [#1649], amélioration de la mémorisation des paramètres de recherche dans la liste des opérateurs [#1613], et affichage des anomalies directement au sein des formulaires [#1599].
- **Corrections d'interface et de logique** : Correction de l'affichage des bordures d'accordéons [#1636], gestion des chevauchements d'en-têtes [#1623], ajustement de la tolérance pour la durée des actes dans les anomalies [#1622] et correction de la récupération des codes DNA pour les structures [#1628].

### Évolutions techniques
- **Optimisation des performances** : Migration de la récupération de données vers les *React Server Components* (RSC) pour la liste des structures [#1633], les fiches structures [#1629] et les CPOM [#1626].
- **Refactorisation et nettoyage** : Simplification de la manipulation des paramètres de recherche [#1615], clarification de l'usage des départements pour les structures [#1601], suppression de références obsolètes (prahdas [#1645]) et renommage de classes internes [#1627].
- **Outils de développement et tests** : Refonte complète et amélioration de la cohérence des données de test (*seeders*) [#1585, #1606, #1616, #1617, #1619, #1620] et correction des tests unitaires [#1621].
- **Analytique** : Mise en place du suivi des exports [#1630] et remplacement de l'outil de suivi Matomo [#1618].

### Autres changements
- **Documentation** : Mise à jour du fichier README en supprimant les instructions opérateurs obsolètes [#1638].
