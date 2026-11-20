## Changelog : maestro (30 derniers jours, au 19 novembre 2026)

### Résumé
Ce mois a été marqué par un enrichissement important des capacités de programmation et de paramétrage, notamment avec l'introduction de la gestion départementale et de la notion de délégation. L'expérience utilisateur a également été améliorée grâce à l'intégration de cartes IGN, de nouveaux composants d'interface et une meilleure gestion des exports de données.

### Évolutions fonctionnelles
- **Programmation et planification** : Gestion de la programmation au niveau départemental [#1751], ajout d'un bouton pour initier de nouvelles saisons [#1716], mise en place de mises à jour groupées pour optimiser la connexion [#1779] et corrections sur l'export et l'affichage des sous-plans [#1664, #1834, #1835, #1855].
- **Paramétrage et descripteurs** : Introduction de la notion de délégation [#1804], support des nombres décimaux [#1756] et des listes à choix multiples [#1755] pour les descripteurs, gestion des quantités maximales d'échantillonnage [#1787] et amélioration de la recherche de descripteurs [#1824].
- **Gestion des utilisateurs** : Ajout des abattoirs sur les fiches utilisateurs [#1797], possibilité de s'ajouter soi-même à la liste des utilisateurs [#1796] et ajout de la fonction d'export des utilisateurs pour les administrateurs [#1826].
- **Interface et visualisation** : Remplacement de MapTiler par des cartes IGN [#1792], support du Markdown pour les messages du tableau de bord [#1805] et ajout d'un nouveau composant de sélection multiple [#1790].
- **Analyse et prélèvements** : Génération automatique des prescriptions lors de la création de sous-plans [#1713], enrichissement des exports de prélèvements avec de nouvelles colonnes (nat, domaine, plan, etc.) [#1825] et support du format ODS pour l'import de la programmation [#1814].
- **Notifications et communication** : Optimisation des notifications Tchap [#1752, #1753] et ajustement des alertes de support lors de l'ajout de préleveurs [#1742].

### Évolutions techniques
- **Sécurité et infrastructure** : Mise en place d'une nouvelle politique de sécurité [#1785], passage à la dernière version LTS de Node.js [#1774] et optimisation de l'environnement Docker pour browserless [#1846].
- **CI/CD et tests** : Optimisation des pipelines de tests via la limitation du nombre de jobs et du déclenchement des tests [#1741, #1743, #1750].
- **Refactoring** : Suppression du code obsolète concernant les enquêtes laboratoires [#1791].

### Autres changements
- Suppression de fonctions de conversion inutiles dans les validateurs XML [#1866].
