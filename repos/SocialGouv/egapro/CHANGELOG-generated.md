## Changelog : egapro (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois a été marqué par un effort majeur de renforcement de la sécurité et de mise en conformité de la plateforme. L'accessibilité numérique (RGAA) a été considérablement améliorée pour garantir une expérience inclusive. Côté utilisateur, la clarté des données a été optimisée (notamment sur les écarts de rémunération) et de nouvelles fonctionnalités de gestion documentaire ont été introduites. En coulisses, le projet prépare une montée en puissance technique avec la transition vers PostgreSQL V2.

### Évolutions fonctionnelles
- **Amélioration de l'accessibilité (RGAA) :** Travaux massifs pour rendre l'interface plus inclusive (navigation au clavier, compatibilité avec le zoom, structuration des tableaux et des graphiques, et gestion des messages d'état) [#4607](https://github.com/SocialGouv/egapro/issues/4607), [#4592](https://github.com/SocialGouv/egapro/issues/4592), [#4614](https://github.com/SocialGouv/egapro/issues/4614).
- **Clarté des données et indicateurs :** 
    - Affichage systématique du sens des écarts sur toutes les vues [#4792](https://github.com/SocialGouv/egapro/issues/4792).
    - Harmonisation de l'affichage des chiffres (troncation à 2 décimales pour éviter les incohérences) [#4730](https://github.com/SocialGouv/egapro/issues/4730), [#4785](https://github.com/SocialGouv/egapro/issues/4785).
    - Mise à jour des libellés pour plus de précision (indicateur G, effectifs, termes de transmission) [#4817](https://github.com/SocialGouv/egapro/issues/4817), [#4728](https://github.com/SocialGouv/egapro/issues/4728).
- **Nouvelles fonctionnalités et gestion :**
    - Nouveau design pour le PDF des données préremplies [#4830](https://github.com/SocialGouv/egapro/issues/4830).
    - Possibilité de déposer un rapport d'évaluation conjointe en cas de mise en demeure dans l'espace personnel [#4825](https://github.com/SocialGouv/egapro/issues/4825).
    - Gestion optimisée des entreprises étrangères et des échéances par démarche [#4735](https://github.com/SocialGouv/egapro/issues/4735), [#4742](https://github.com/SocialGouv/egapro/issues/4742).
- **Conformité légale :** Mise en place de CGU versionnées et d'une nouvelle politique de confidentialité [#4828](https://github.com/SocialGouv/egapro/issues/4828).

### Évolutions techniques
- **Sécurité renforcée :**
    - Mise en place de mesures de protection robustes : en-têtes HTTP de sécurité, politique de sécurité du contenu (CSP) et protection contre le CSRF [#4763](https://github.com/SocialGouv/egapro/issues/4763), [#4755](https://github.com/SocialGouv/egapro/issues/4755).
    - Sécurisation des accès : restriction de l'administration aux agents publics, nouveaux modes de double authentification (2FA) et protection des endpoints d'export [#4760](https://github.com/SocialGouv/egapro/issues/4760), [#4816](https://github.com/SocialGouv/egapro/issues/4816), [#4753](https://github.com/SocialGouv/egapro/issues/4753).
    - Protection contre les abus : limitation du débit (rate limiting) et anonymisation des données envoyées aux outils de suivi (Sentry) [#4762](https://github.com/SocialGouv/egapro/issues/4762), [#4902](https://github.com/SocialGouv/egapro/issues/4902).
- **Infrastructure et Architecture :**
    - Préparation de la migration vers PostgreSQL V2 [#4824](https://github.com/SocialGouv/egapro/issues/4824).
    - Refactoring de l'API publique pour limiter l'exposition des données de consultation [#4793](https://github.com/SocialGouv/egapro/issues/4793).
    - Optimisation de la CI/CD : intégration de tests Lighthouse, amélioration des tests de bout en bout (e2e) et sécurisation des processus de fusion [#4867](https://github.com/SocialGouv/egapro/issues/4867), [#4829](https://github.com/SocialGouv/egapro/issues/4829).

### Autres changements
- **Documentation :** Publication des règles relatives à la génération des journaux d'action et à leurs durées de conservation [#4774](https://github.com/SocialGouv/egapro/issues/4774).
